"""Harvest OAI feeds from Islandora, DSpace, Other to get resource IDs."""
import requests
import httplib
import time
import re
import os
from lxml import etree
from argparse import ArgumentParser
ns = {"mods": 'http://www.loc.gov/mods/v3',
      "oai": 'http://www.openarchives.org/OAI/2.0/'}


def getIDs(link, command, verbose=1, sleepTime=2):
    """Call requests to get OAI feed or handle errors."""
    if sleepTime:
        time.sleep(sleepTime)
    remoteAddr = link + '?verb=%s' % command
    if verbose:
        print("\r", "getIDs ...'%s'" % remoteAddr[-90:])

    # call the OAI-PMH HTTP endpoint, print error if problem.
    try:
        remoteData = requests.get(remoteAddr).content
        # See if OAI-PMH response has any errors.
        mo = re.search('<error *code=\"([^"]*)">(.*)</error>', remoteData)
        if mo:
            print("OAIERROR: code=%s '%s'" % (mo.group(1), mo.group(2)))
        else:
            return(remoteData)
    except httplib.IncompleteRead as e:
        page = e.partial
        print(page)
    except Exception as exValue:
        print(exValue)


if __name__ == "__main__":
    """Main module for handling OAI, commands, calling request."""
    parser = ArgumentParser()
    parser.add_argument("-l", "--link", dest="link", help="OAI-PMH URL")
    parser.add_argument("-o", "--filename", dest="filename",
                        help="write repository to file", default="output.xml")
    parser.add_argument("-f", "--from", dest="fromDate",
                        help="harvest records from this date yyyy-mm-dd")
    parser.add_argument("-u", "--until", dest="until",
                        help="harvest records until this date yyyy-mm-dd")
    parser.add_argument("-m", "--mdprefix", dest="mdprefix", default="oai_dc",
                        help="use the specified metadata format")
    parser.add_argument("-s", "--setName", dest="setName",
                        help="harvest the specified set")
    args = parser.parse_args()

    if not args.link.startswith('http'):
        args.link = 'http://' + args.link
    print("Writing records to %s from %s" % (args.filename, args.link))
    verbOpts = ''
    if args.setName:
        verbOpts += '&set=%s' % args.setName
    if args.fromDate:
        verbOpts += '&from=%s' % args.fromDate
    if args.until:
        verbOpts += '&until=%s' % args.until
    if args.mdprefix:
        verbOpts += '&metadataPrefix=%s' % args.mdprefix

    print("Using url:%s" % args.link + '?ListRecords' + verbOpts)
    data = getIDs(args.link, 'ListRecords' + verbOpts)
    writedir = "../yudl_mods/" + time.strftime("%Y%m%d") + "/"
    if not os.path.exists(writedir):
        os.makedirs(writedir)

    # from http://boodebr.org/main/python/all-about-python-and-unicode#UNI_XML
    RE_XML_IL = u'([\u0000-\u0008\u000b-\u000c\u000e-\u001f\ufffe-\uffff])' + \
                u'|' + \
                u'([%s-%s][^%s-%s])|([^%s-%s][%s-%s])|([%s-%s]$)|(^[%s-%s])' %\
                (unichr(0xd800), unichr(0xdbff), unichr(0xdc00),
                 unichr(0xdfff), unichr(0xd800), unichr(0xdbff),
                 unichr(0xdc00), unichr(0xdfff), unichr(0xd800),
                 unichr(0xdbff), unichr(0xdc00), unichr(0xdfff))
    dataClean = re.sub(RE_XML_IL, "?", data)

    recordCount = 0
    sets = set()
    while dataClean:
        feed = etree.fromstring(dataClean)
        for rec in feed.iter("{http://www.openarchives.org/OAI/2.0/}record"):
            header = rec.find("oai:header", namespaces=ns)
            rec_id = header.find("oai:identifier", namespaces=ns).text
            setSpec = header.find("oai:setSpec", namespaces=ns).text
            if "oai:yul:" in rec_id:
                rec_id = rec_id.replace('oai:yul:', "")
                rec_id = rec_id.replace("_", ":")
                setSpec = setSpec.replace("_", ":")
                sets.add(setSpec)
            with open(writedir + setSpec + ".txt", "a") as ofile:
                ofile.write(rec_id + "\n")
            recordCount += 1
        more = re.search('<resumptionToken[^>]*>(.*)</resumptionToken>',
                         dataClean)
        if not more:
            break
        data = getIDs(args.link, "ListRecords&resumptionToken=%s" %
                      more.group(1))
        dataClean = re.sub(RE_XML_IL, "?", data)
    print("Wrote out %d records in %d sets." % (recordCount, len(sets)))
