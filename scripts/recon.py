"""Script for analyzing MODS records harvested from YUL Dig Collections."""
import sys
from argparse import ArgumentParser
from lxml import etree
import urllib
import requests
import app
import os
import fuzz
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

    def get_xpath(self):
        out = []
        if self.elem is not None:
            if self.elem.xpath(self.args.xpath, namespaces=ns) is not None:
                for value in self.elem.xpath(self.args.xpath, namespaces=ns):
                    if value.text is not None:
                        out.append(value.text.encode("utf-8").strip())
            if len(out) == 0:
                out = None
            self.elements = out
            return self.elements


def recon(value):
    """Reconciliation matching."""
    uri = None
    query = value.strip()
    try:
        url = ('http://id.loc.gov/subjects/suggest/?q=' +
               urllib.parse.quote(query.encode('utf8')))
        app.logger.debug("LC Authorities API url is " + url)
        resp = requests.get(url)
        results = resp.json()

    for n in range(0, len(results[1])):
        name = results[1][n]
        uri = results[3][n]
        score = fuzz.token_sort_ratio(query, name)
        if score > 80:
            app.logger.debug("Label is " + name + " Score is " + str(score) +
                             " URI is " + uri)
            return(uri)

    # Get the results for the didyoumean API (cross-refs, no primary headings)
    if score < 60:
        url = ('http://id.loc.gov/subjects/didyoumean/?label=' +
               urllib.parse.quote(query.encode('utf8')))
        app.logger.debug("LC Authorities API url is " + url)
        altresp = requests.get(url)
        altresults = etree.fromstring(altresp.content)
        app.logger.debug("LC Authorities API url is " + url)
        altresp = requests.get(url)
        altresults = etree.fromstring(altresp.content)

    for child in altresults.iter('{http://id.loc.gov/ns/id_service#}term'):
        match = False
        name = child.text
        uri = child.get('uri')
        score = fuzz.token_sort_ratio(query, name)
        app.logger.debug("Label is " + name + " Score is " + str(score) +
                         " URI is " + uri)
        if score > 80:
            app.logger.debug("Label is " + name + " Score is " + str(score) +
                             " URI is " + uri)
            return(uri)


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


def main():
    parser = ArgumentParser(usage='%(prog)s [options] filename.xml')
    parser.add_argument("-e", "--element", dest="element",
                        help="return element values")
    parser.add_argument("-x", "--xpath", dest="xpath",
                        help="recon element xpath location")
    parser.add_argument("datafile", help="XML files or directory")

    args = parser.parse_args()

    if not len(sys.argv) > 0:
        parser.print_help()
        parser.exit()

    if args.element is None and args.xpath is None:
        args.stats = True

    files = set()
    if os.path.isfile(args.datafile):
        if args.filename.endswith('.xml'):
            files.add(args.datafile)
    elif os.path.isdir(args.datafile):
        for filename in os.listdir(args.datafile):
            if filename.endswith('.xml'):
                files.add(args.datafile + "/" + filename)

    for sourcefile in files:
        parser = etree.ETCompatXMLParser()
        try:
            feed = etree.parse(open(sourcefile, 'r'), parser)
        except etree.XMLSyntaxError as e:
            print(sourcefile, e)
        for rec in feed.iter(MODS_NAMESPACE + "mods"):
            r = Record(rec, args)
            record_id = sourcefile.replace('.mods.xml', '')
            if "/" in record_id:
                record_id = record_id.split("/")[-1]

            if args.xpath is not None:
                if r.get_xpath() is not None:
                    for i in r.get_xpath():
                        print(str(i.decode()))
            rec.clear()

if __name__ == "__main__":
    main()
