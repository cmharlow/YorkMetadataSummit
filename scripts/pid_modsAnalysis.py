"""Script for analyzing MODS records harvested from YUL Dig Collections."""
import sys
from argparse import ArgumentParser
from lxml import etree
import requests
import os
import time
MODS_NAMESPACE = "{http://www.loc.gov/mods/v3}"
ns = {"mods": 'http://www.loc.gov/mods/v3'}


class RepoInvestigatorException(Exception):
    """This is our base exception for this script."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "%s" % (self.value,)


class Record:
    """Base class for a MODS or nested metadata record."""

    def __init__(self, elem, args):
        self.elem = elem
        self.args = args

    def get_elements(self):
        out = []
        if self.elem is not None:
            for desc in self.elem.iterdescendants():
                if desc.tag == MODS_NAMESPACE + self.args.element and desc.text is not None:
                    out.append(desc.text.encode("utf-8").strip())
            if len(out) == 0:
                out = None
            self.elements = out
            return self.elements

    def get_xpath(self):
        out = []
        if self.elem is not None:
            if self.elem.xpath(self.args.xpath, namespaces=ns) is not None:
                for value in self.elem.xpath(self.args.xpath, namespaces=ns):
                    if value.text is not None:
                        out.append(value.text.strip())
            if len(out) == 0:
                out = None
            self.elements = out
            return self.elements

    def get_stats(self):
        stats = {}
        for child in self.elem:
            val = linearize(child, "mods:mods/" + removeNS(child.tag))
            stats.setdefault(val, 0)
            stats[val] += 1
        return stats

    def has_element(self):
        present = False
        if self.elem is not None:
            for desc in self.elem.iterdescendants():
                if desc.tag == MODS_NAMESPACE + self.args.element and desc.text is not None:
                    present = True
                    return present

    def has_xpath(self):
        present = False
        if self.elem is not None:
            if self.elem.xpath(self.args.xpath, namespaces=ns) is not None:
                for value in self.elem.xpath(self.args.xpath, namespaces=ns):
                    if value.text is not None:
                        present = True
                        return present


def removeNS(tag):
    if tag.find('}') == -1:
        return tag
    else:
        return tag.replace("{http://www.loc.gov/mods/v3}", "mods:")


def linearize(el, path):
    # Print text value if not empty
    if el.text is not None:
        text = el.text.strip()
    else:
        text = el.text
    if text is not None and el.items() is []:
        return(path)
    elif el.items() is not []:
        attribpath = path
        for name, val in el.items():
            # Print attributes
            attribpath += ("[@" + removeNS(name) + "=" + val + "]")
        if text is not None and len(el) == 0:
            return(attribpath)
        elif text is not None and len(el) > 0:
            for childEl in el:
                tag = removeNS(childEl.tag)
                # Print child node recursively
                newval = linearize(childEl, attribpath + '/' + tag)
                return(newval)


def collect_stats(stats_aggregate, stats):
    """increment the record counter."""
    stats_aggregate["record_count"] += 1

    for field in stats:
        # get the total number of times a field occurs
        stats_aggregate["field_info"].setdefault(field, {"field_count": 0})
        stats_aggregate["field_info"][field]["field_count"] += 1

        # get average of all fields
        stats_aggregate["field_info"][field].setdefault("field_count_total", 0)
        stats_aggregate["field_info"][field]["field_count_total"] += stats[field]


def create_stats_averages(stats_aggregate):
    for field in stats_aggregate["field_info"]:
        field_count = stats_aggregate["field_info"][field]["field_count"]
        field_count_total = stats_aggregate["field_info"][field]["field_count_total"]

        field_count_total_average = (float(field_count_total) / float(stats_aggregate["record_count"]))
        stats_aggregate["field_info"][field]["field_count_total_average"] = field_count_total_average

        field_count_element_average = (float(field_count_total) / float(field_count))
        stats_aggregate["field_info"][field]["field_count_element_average"] = field_count_element_average
    return stats_aggregate


def calc_completeness(stats_averages):
    completeness = {}
    record_count = stats_averages["record_count"]
    completeness_total = 0
    wwww_total = 0
    collection_total = 0
    collection_field_to_count = 0

    wwww = [
        'mods:name/mods:namePart',       # who
        'mods:titleInfo/mods:title',         # what
        'mods:identifier',    # where
        'mods:originInfo/mods:dateCreated'           # when
    ]

    for element in sorted(stats_averages["field_info"]):
            element_completeness_percent = 0
            element_completeness_percent = ((stats_averages["field_info"][element]["field_count"] / float(record_count)) * 100)
            completeness_total += element_completeness_percent
            # gather collection completeness
            if element_completeness_percent > 10:
                collection_total += element_completeness_percent
                collection_field_to_count += 1
            # gather wwww completeness
            if element in wwww:
                wwww_total += element_completeness_percent

    completeness["collection_completeness"] = collection_total / float(collection_field_to_count)
    completeness["wwww_completeness"] = wwww_total / float(len(wwww))
    completeness["average_completeness"] = ((completeness["collection_completeness"] + completeness["wwww_completeness"]) / float(4))
    return completeness


def pretty_print_stats(stats_averages):
    record_count = stats_averages["record_count"]
    # get header length
    element_length = 0
    for element in stats_averages["field_info"]:
        if element_length < len(element):
            element_length = len(element)

    print("\n\n")
    for element in sorted(stats_averages["field_info"]):
        percent = (stats_averages["field_info"][element]["field_count"] / float(record_count)) * 100
        percentPrint = "=" * (int((percent) / 4))
        columnOne = " " * (element_length - len(element)) + element
        print("%s: |%-25s| %6s/%s | %3d%% " % (
                    columnOne,
                    percentPrint,
                    stats_averages["field_info"][element]["field_count"],
                    record_count,
                    percent
                ))

    print("\n")
    completeness = calc_completeness(stats_averages)
    for i in ["collection_completeness", "wwww_completeness", "average_completeness"]:
        print("%23s %f" % (i, completeness[i]))


def main():
    stats_aggregate = {
        "record_count": 0,
        "field_info": {}
    }

    parser = ArgumentParser(usage='%(prog)s [options] PIDs_filename.txt')
    parser.add_argument("-e", "--element", dest="element",
                        help="return element values")
    parser.add_argument("-x", "--xpath", dest="xpath",
                        help="get response of xpath expression on mods:mods")
    parser.add_argument("-i", "--id", action="store_true", dest="id",
                        default=False, help="prepend meta_id to line")
    parser.add_argument("-s", "--stats", action="store_true", dest="stats",
                        default=False, help="only print stats for repository")
    parser.add_argument("-p", "--present", action="store_true", dest="present",
                        default=False, help="If element has value in record")
    parser.add_argument("datafile", help="PIDs textfiles or directory")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    if args.element is None and args.xpath is None:
        args.stats = True

    pids = []
    if os.path.isfile(args.datafile):
        with open(args.datafile) as fh:
            pids.extend(fh.read().splitlines())
    elif os.path.isdir(args.datafile):
        for filename in os.listdir(args.datafile):
            with open(filename) as fh:
                pids.extend(fh.read().splitlines())

    s = 0
    for pid in pids:
        url = "http://digital.library.yorku.ca/islandora/object/"
        url += pid + "/datastream/MODS"
        modsxml = requests.get(url)
        time.sleep(1)
        feed = etree.fromstring(modsxml.content)
        for rec in feed.iter(MODS_NAMESPACE + "mods"):
            r = Record(rec, args)
            record_id = pid
            if args.stats is False and args.present is False and args.element is not None:
                if r.get_elements() is not None:
                    for i in r.get_elements():
                        if args.id:
                            print("\t".join([record_id, str(i.decode())]))
                        else:
                            print(i)

            if args.stats is False and args.present is False and args.xpath is not None:
                if r.get_xpath() is not None:
                    for i in r.get_xpath():
                        if args.id:
                            print("\t".join([str(record_id), str(i.decode())]))
                        else:
                            print(str(i.decode()))

            if args.stats is False and args.element is not None and args.present is True:
                print("%s %s" % (record_id, r.has_element()))

            if args.stats is False and args.xpath is not None and args.present is True:
                print("%s %s" % (record_id, r.has_xpath()))

            if args.stats is True and args.element is None:
                if (s % 100) == 0 and s != 0:
                    print("%d records processed" % s)
                s += 1
                collect_stats(stats_aggregate, r.get_stats())
            rec.clear()

    if args.stats is True and args.element is None:
        stats_averages = create_stats_averages(stats_aggregate)
        pretty_print_stats(stats_averages)

if __name__ == "__main__":
    main()
