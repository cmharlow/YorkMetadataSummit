York University Libraries Digital Collections Metadata Report
-------------------------------------------------------------

Author: Christina Harlow, cmharlow@gmail.com
Date: November 2016
Prepared for: York University Libraries
License: CC0

Table of Contents
=================

1. Introduction and Scope of this Report
2. Digital Collections Existing Metadata Analysis
3. Digital Collections Metadata Enhancements
4. Converting XML-based Metadata to RDF
5. Supporting a RDF Ecosystem for Digital Collections
6. Conclusions & Steps Forward

I. Introduction and Scope of this Report
========================================

This Report represents work and outcomes from a 2-day Metadata Summit at the York University Libraries. It is meant to capture, describe, and give ideas for moving many of the discussions points and goals surfaced at the YUL Metadata Summit Forward.

The York University Libraries Metadata Summit arose from having an outsider come in, assess current practices and outcomes in digital collections metadata work, and guide a staff-supported dialog in moving metadata practices forward. This included a review ...

Something about the review done during the event.

Outsider to view all the local expertise across subdomains.

Focus is digital collections, namely, Islandora collections. Looking at stuff moving forward.

- Digital Collections
- Looking Outward (ecosystem)
- Looking Forward (RDF)
- Leveraging Existing Workflows and Expertise


II. Digital Collections Existing Metadata Analysis
==================================================

- Current Ecosystem
    - Islandora / Fedora
    - Dspace Migration
    - MODS/XML (Object Description)
    - RELS-EXT (Object Structure)
    - Other datastreams in Fedora?
    - Ingest & Output
- Analysis Methods
    - Python scripts
    - How to run
    - Sample workflow
    - What the output means
- Analysis Reports
    - Reports run on November 2016
    - Field Usage/Appearance
    - Common Facet or Search Field Reports
    - Object Structure Report

```bash

                                                                                                                              mods:mods/mods:abstract: |=======================  |  25945/27133 |  95%
                                                                                                                       mods:mods/mods:accessCondition: |                         |     48/27133 |   0%
                                                                                            mods:mods/mods:accessCondition[@type=restrictionOnAccess]: |                         |     16/27133 |   0%
                                                                                           mods:mods/mods:accessCondition[@type=use and reproduction]: |                         |    758/27133 |   2%
                                                                                             mods:mods/mods:accessCondition[@type=useAndReproduction]: |=======================  |  25272/27133 |  93%
                                                                                                        mods:mods/mods:classification[@authority=ddc]: |                         |     13/27133 |   0%
                                                                                           mods:mods/mods:classification[@authority=ddc][@edition=19]: |                         |     10/27133 |   0%
                                                                                           mods:mods/mods:classification[@authority=ddc][@edition=22]: |                         |      1/27133 |   0%
                                                                                                        mods:mods/mods:classification[@authority=lcc]: |                         |    243/27133 |   0%
                                                                                                        mods:mods/mods:classification[@authority=udc]: |                         |      1/27133 |   0%
                                                                                                                                 mods:mods/mods:genre: |                         |    569/27133 |   2%
                                                                                                               mods:mods/mods:genre[@authority=lctgm]: |=======================  |  25601/27133 |  94%
                                                                                                              mods:mods/mods:genre[@authority=marcgt]: |                         |    304/27133 |   1%
                                                                                                                            mods:mods/mods:identifier: |                         |    427/27133 |   1%
                                                                                                                 mods:mods/mods:identifier[@type=hdl]: |======================   |  24286/27133 |  89%
                                                                                                                mods:mods/mods:identifier[@type=isbn]: |                         |      4/27133 |   0%
                                                                                                                mods:mods/mods:identifier[@type=issn]: |                         |      9/27133 |   0%
                                                                                                                mods:mods/mods:identifier[@type=lccn]: |                         |    147/27133 |   0%
                                                                                                  mods:mods/mods:identifier[@type=lccn][@invalid=yes]: |                         |      1/27133 |   0%
                                                                                                               mods:mods/mods:identifier[@type=local]: |=======================  |  25851/27133 |  95%
                                                                                                                mods:mods/mods:identifier[@type=oclc]: |                         |     55/27133 |   0%
                                                                                                               mods:mods/mods:identifier[@type=other]: |                         |    939/27133 |   3%
                                                                                                        mods:mods/mods:identifier[@type=stock number]: |                         |      2/27133 |   0%
                                                                                                                 mods:mods/mods:identifier[@type=url]: |                         |      5/27133 |   0%
                                                                                                                              mods:mods/mods:language: |                         |     22/27133 |   0%
                                                                          mods:mods/mods:language/mods:languageTerm[@authority=iso639-2b][@type=code]: |=====                    |   5543/27133 |  20%
                                         mods:mods/mods:language[@objectPart=summary or subtitle]/mods:languageTerm[@authority=iso639-2b][@type=code]: |                         |      7/27133 |   0%
                                                 mods:mods/mods:language[@objectPart=translation]/mods:languageTerm[@authority=iso639-2b][@type=code]: |                         |     12/27133 |   0%
                                                                                                        mods:mods/mods:location/mods:physicalLocation: |=======================  |  25489/27133 |  93%
                                                                                                                     mods:mods/mods:location/mods:url: |                         |     27/27133 |   0%
                                                                                          mods:mods/mods:location/mods:url[@displayLabel=Active site]: |                         |    215/27133 |   0%
                                                          mods:mods/mods:location/mods:url[@displayLabel=electronic resource][@usage=primary display]: |                         |      8/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."10, no.1" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."14, no.6" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."15, no.1" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."16, no.3" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."22, no.3" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."23, no.8" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."24, no.5" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."24, no.8" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."30, no.3" Internet_Archive]: |                         |      3/27133 |   0%
                                              mods:mods/mods:location/mods:url[@displayLabel=vol."30, no.4" Internet_Archive][@usage=primary display]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."32, no.4" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."33, no.1" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."34, no.1" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."34, no.7" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."35, no.2" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."35, no.4" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."35, no.6" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."36, no.8" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."37, no.7" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."37, no.9" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."38, no.4" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."38, no.8" Internet_Archive]: |                         |      3/27133 |   0%
                                                                      mods:mods/mods:location/mods:url[@displayLabel=vol."40, no.2" Internet_Archive]: |                         |      3/27133 |   0%
                                                                     mods:mods/mods:location/mods:url[@displayLabel=vol."41, no.10" Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.42 n.03 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.42 n.04 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.43 n.01 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.44 n.05 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.44 n.06 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.44 n.08 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.44 n.11 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.44 n.12 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.45 n.05 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.46 n.06 Internet_Archive]: |                         |      3/27133 |   0%
                                                                              mods:mods/mods:location/mods:url[@displayLabel=vol.48 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.49 n.08 Internet_Archive]: |                         |      3/27133 |   0%
                                                                         mods:mods/mods:location/mods:url[@displayLabel=vol.51 n.02 Internet_Archive]: |                         |      3/27133 |   0%
                                                                                                                    mods:mods/mods:name/mods:namePart: |===                      |   3660/27133 |  13%
                                                                      mods:mods/mods:name/mods:role/mods:roleTerm[@authority=marcrelator][@type=text]: |                         |     75/27133 |   0%
                                                                                mods:mods/mods:name/mods:roleTerm[@authority=marcrelator][@type=text]: |                         |     84/27133 |   0%
                                                                 mods:mods/mods:name[@nameTitleGroup=1][@type=personal][@usage=primary]/mods:namePart: |                         |      3/27133 |   0%
                                                                                                mods:mods/mods:name[@type=corporate]/mods:affiliation: |                         |      2/27133 |   0%
                                                                                                   mods:mods/mods:name[@type=corporate]/mods:namePart: |                         |    535/27133 |   1%
          mods:mods/mods:name[@type=corporate][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/68925562]/mods:namePart: |                         |      1/27133 |   0%
         mods:mods/mods:name[@type=corporate][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/71477633/]/mods:namePart: |                         |      2/27133 |   0%
                                                                                mods:mods/mods:name[@type=corporate][@nameTitleGroup=1]/mods:namePart: |                         |     11/27133 |   0%
                                                                                                 mods:mods/mods:name[@type=personal]/mods:affiliation: |                         |     32/27133 |   0%
                                                                                                    mods:mods/mods:name[@type=personal]/mods:namePart: |==                       |   2629/27133 |   9%
                                                      mods:mods/mods:name[@type=personal]/mods:role/mods:roleTerm[@authority=marcrelator][@type=text]: |                         |      3/27133 |   0%
mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=Permalink: http://viaf.org/viaf/71477633]/mods:namePart: |                         |      1/27133 |   0%
          mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/112774103]/mods:namePart: |                         |     14/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/11807535]/mods:namePart: |                         |     27/27133 |   0%
          mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/139973271]/mods:namePart: |                         |      2/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/29543057]/mods:namePart: |                         |     85/27133 |   0%
            mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/3252348]/mods:namePart: |                         |      4/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/36868311]/mods:namePart: |                         |      2/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/44318353]/mods:namePart: |                         |      2/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/61541730]/mods:namePart: |                         |      2/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/67239096]/mods:namePart: |                         |      1/27133 |   0%
          mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/71477633/]/mods:namePart: |                         |     10/27133 |   0%
           mods:mods/mods:name[@type=personal][@authority=viaf][@authorityURI=http://viaf.org][@valueURI=http://viaf.org/viaf/71477633]/mods:namePart: |                         |     24/27133 |   0%
                                                                                    mods:mods/mods:name[@type=personal][@usage=primary]/mods:namePart: |                         |    544/27133 |   2%
                                                                 mods:mods/mods:name[@type=personal][@usage=primary][@nameTitleGroup=1]/mods:namePart: |                         |     11/27133 |   0%
                                                                                                                                  mods:mods/mods:note: |=======================  |  25215/27133 |  92%
                                                                              mods:mods/mods:note[@altRepGroup=00][@type=statement of responsibility]: |                         |     70/27133 |   0%
                                                                                                  mods:mods/mods:note[@type=additional physical form]: |                         |     11/27133 |   0%
                                                                                                              mods:mods/mods:note[@type=bibliography]: |                         |     67/27133 |   0%
                                                                                               mods:mods/mods:note[@type=date/sequential designation]: |                         |     23/27133 |   0%
                                                                                                            mods:mods/mods:note[@type=formsPartOfPDF]: |                         |     32/27133 |   0%
                                                                                                            mods:mods/mods:note[@type=formsPartOfTIF]: |                         |    148/27133 |   0%
                                                                                                                   mods:mods/mods:note[@type=funding]: |                         |    160/27133 |   0%
                                                                                                                  mods:mods/mods:note[@type=language]: |                         |     11/27133 |   0%
                                                                                                                 mods:mods/mods:note[@type=numbering]: |                         |     14/27133 |   0%
                                                                                                                 mods:mods/mods:note[@type=ownership]: |==                       |   2680/27133 |   9%
                                                                                                              mods:mods/mods:note[@type=reproduction]: |                         |      6/27133 |   0%
                                                                              mods:mods/mods:note[@type=statement of responsibility][@altRepGroup=00]: |                         |    365/27133 |   1%
                                                                                                                    mods:mods/mods:note[@type=thesis]: |                         |      1/27133 |   0%
                                                                                                                  mods:mods/mods:note[@type=titleSrc]: |                         |    448/27133 |   1%
                                                                                                             mods:mods/mods:note[@type=transcription]: |                         |     16/27133 |   0%
                                                                                                                      mods:mods/mods:note[@type=with]: |                         |     19/27133 |   0%
                                                                                                         mods:mods/mods:originInfo/mods:copyrightDate: |                         |      9/27133 |   0%
                                                                                                          mods:mods/mods:originInfo/mods:dateCaptured: |                         |    216/27133 |   0%
                                                                                                           mods:mods/mods:originInfo/mods:dateCreated: |======================   |  24816/27133 |  91%
                                                                                                            mods:mods/mods:originInfo/mods:dateIssued: |                         |    289/27133 |   1%
                                                                                            mods:mods/mods:originInfo/mods:dateIssued[@encoding=marc]: |                         |      1/27133 |   0%
                                                                                           mods:mods/mods:originInfo/mods:dateIssued[@script=Burmese]: |                         |      3/27133 |   0%
                                                                                                             mods:mods/mods:originInfo/mods:dateOther: |                         |    581/27133 |   2%
                                                                                                              mods:mods/mods:originInfo/mods:issuance: |                         |     42/27133 |   0%
                                                                          mods:mods/mods:originInfo/mods:place/mods:placeTerm[@authority=marccountry]: |                         |      9/27133 |   0%
                                                              mods:mods/mods:originInfo/mods:place/mods:placeTerm[@authority=marccountry][@type=code]: |                         |     72/27133 |   0%
                                                              mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type=code][@authority=marccountry]: |                         |    393/27133 |   1%
                                                                                      mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type=text]: |                         |    228/27133 |   0%
                                                                                                             mods:mods/mods:originInfo/mods:publisher: |                         |      8/27133 |   0%
                                                                                                                   mods:mods/mods:physicalDescription: |                         |     11/27133 |   0%
                                                                                                       mods:mods/mods:physicalDescription/mods:extent: |                         |      6/27133 |   0%
                                                                                                         mods:mods/mods:physicalDescription/mods:form: |===                      |   3869/27133 |  14%
                                                                                mods:mods/mods:physicalDescription/mods:form[@authority=marccategory]: |                         |     23/27133 |   0%
                                                                                    mods:mods/mods:physicalDescription/mods:form[@authority=marcform]: |=====================    |  23128/27133 |  85%
                                                                                                                      mods:mods/mods:physicalLocation: |                         |      6/27133 |   0%
                                                                                                   mods:mods/mods:recordInfo/mods:descriptionStandard: |                         |    333/27133 |   1%
                                                                               mods:mods/mods:recordInfo/mods:recordContentSource[@authority=marcorg]: |                         |     69/27133 |   0%
                                                                                    mods:mods/mods:recordInfo/mods:recordCreationDate[@encoding=marc]: |                         |    321/27133 |   1%
                                                                                                 mods:mods/mods:relatedItem/mods:titleInfo/mods:title: |=======================  |  25601/27133 |  94%
                                                                              mods:mods/mods:relatedItem[@type=constituent]/mods:titleInfo/mods:title: |                         |     14/27133 |   0%
                                                                                        mods:mods/mods:relatedItem[@type=host]/mods:location/mods:url: |                         |      1/27133 |   0%
                                                                                           mods:mods/mods:relatedItem[@type=host]/mods:part/mods:date: |                         |     10/27133 |   0%
                                                                                         mods:mods/mods:relatedItem[@type=host]/mods:part/mods:extent: |                         |     28/27133 |   0%
                                                                                     mods:mods/mods:relatedItem[@type=host]/mods:titleInfo/mods:title: |                         |    213/27133 |   0%
                                                                           mods:mods/mods:relatedItem[@type=isReferencedBy]/mods:titleInfo/mods:title: |                         |      2/27133 |   0%
                                                                                mods:mods/mods:relatedItem[@type=preceding]/mods:titleInfo/mods:title: |                         |      6/27133 |   0%
                                                                                   mods:mods/mods:relatedItem[@type=series]/mods:titleInfo/mods:title: |                         |     84/27133 |   0%
                                                                               mods:mods/mods:relatedItem[@type=succeeding]/mods:titleInfo/mods:title: |                         |      8/27133 |   0%
                                                                                                               mods:mods/mods:subject/mods:geographic: |                         |     11/27133 |   0%
                                                                                       mods:mods/mods:subject/mods:geographicCode[@authority=marcgac]: |                         |     98/27133 |   0%
                                                                                    mods:mods/mods:subject/mods:hierarchicalGeographic/mods:continent: |                         |    307/27133 |   1%
                                                                                      mods:mods/mods:subject/mods:hierarchicalGeographic/mods:country: |                         |      2/27133 |   0%
                                                                                      mods:mods/mods:subject/mods:name[@type=corporate]/mods:namePart: |                         |      1/27133 |   0%
                                                                                                                    mods:mods/mods:subject/mods:topic: |======================== |  26080/27133 |  96%
                                                                                               mods:mods/mods:subject[@authority=csh]/mods:geographic: |                         |      1/27133 |   0%
                                                                                                   mods:mods/mods:subject[@authority=lcsh]/mods:genre: |                         |      1/27133 |   0%
                                                                                              mods:mods/mods:subject[@authority=lcsh]/mods:geographic: |                         |    116/27133 |   0%
                                                                     mods:mods/mods:subject[@authority=lcsh]/mods:name[@type=corporate]/mods:namePart: |                         |     44/27133 |   0%
                                                                      mods:mods/mods:subject[@authority=lcsh]/mods:name[@type=personal]/mods:namePart: |                         |     55/27133 |   0%
                                                mods:mods/mods:subject[@authority=lcsh]/mods:name[@type=personal]/mods:namePart[@type=termsOfAddress]: |                         |     13/27133 |   0%
                                                                                    mods:mods/mods:subject[@authority=lcsh]/mods:titleInfo/mods:title: |                         |      5/27133 |   0%
                                                                                                   mods:mods/mods:subject[@authority=lcsh]/mods:topic: |                         |    361/27133 |   1%
                                                                                                                       mods:mods/mods:tableOfContents: |                         |    103/27133 |   0%
                                                                                                                        mods:mods/mods:targetAudience: |===                      |   3668/27133 |  13%
                                                                                                                mods:mods/mods:titleInfo/mods:nonSort: |                         |    177/27133 |   0%
                                                                                                                  mods:mods/mods:titleInfo/mods:title: |======================== |  26950/27133 |  99%
                                                                                mods:mods/mods:titleInfo[@nameTitleGroup=1][@type=uniform]/mods:title: |                         |      3/27133 |   0%
                                                                                               mods:mods/mods:titleInfo[@type=alternative]/mods:title: |                         |    198/27133 |   0%
                                                                      mods:mods/mods:titleInfo[@type=alternative][@displayLabel=Cited as:]/mods:title: |                         |      5/27133 |   0%
                                                                                     mods:mods/mods:titleInfo[@type=translated][@lang=eng]/mods:title: |                         |     15/27133 |   0%
                                                                                                   mods:mods/mods:titleInfo[@type=uniform]/mods:title: |                         |      5/27133 |   0%
                                                                                mods:mods/mods:titleInfo[@type=uniform][@nameTitleGroup=1]/mods:title: |                         |     22/27133 |   0%
                                                                                                                        mods:mods/mods:typeOfResource: |======================== |  27105/27133 |  99%
                                                                                                       mods:mods/mods:typeOfResource[@collection=yes]: |                         |      4/27133 |   0%


collection_completeness 75.462482
      wwww_completeness 0.000000
   average_completeness 18.865621
```

### Rights Statements

```
1 "Reproduction of the proceedings of the House of Commons and its Committees, in whole or in part and in any
6 ...
9 All rights reserved
1 Bram Morrison: contacted, permission granted. Sam Hinton: estate contacted, no response as of 30.03.10.
1 CCPA
1 Canadian National||For further copyright information contact : ascproj@yorku.ca
1 Charlie Chin: contacted, permission granted. Chris Iijima: estate contacted, no response as of 02.03.2010.
1 Clara Thomas Archives and Special Collections
58 Clara Thomas Archives and Special Collections http://www.library.yorku.ca/ccm/ArchivesSpecialCollections/StaffComments.htm
1 Clara Thomas Archives and Special Collections http://www.library.yorku.ca/web/archives/ask-a-question/
1 Copyright of images owned by Lou Wise. Geo-spatial data and KML files generated by YUL staff is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. For further copyright and contact information email: ascproj@yorku.ca
1572 Copyright of images owned by Lou Wise. Geo-spatial data and KML files generated by YUL staff is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License. For further copyright and contact information email: ascproj@yorku.ca.
621 Copyright owned by York University. For permission to publish or other copyright questions, contact ascproj@yorku.ca
1 Copyright owned by wire service. For more information contact, ascproj@yorku.ca
1 Copyright remains with the creator.
1 Copyright remains with the creator.   License to reproduce this document without alteration granted by the ILO in August 2015.
1 Copyright remains with the creator.  Permission to reproduce this document granted by Pembina Institute.
1 Copyright remains with the creator.  Reproduced under license from the ILO, granted 2015.
1 Copyright remains with the creator. Reproduced with permission of the Canadian Labour Congress.
1 Copyright remains with the creator; Reproduced with permission of the David Suzuki Foundation.
1 Copyright retained by LNS
2 Copyright retained by the Government of Manitoba
6 Creative Commons
2 Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 License
1 Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 License for all works
1 Crown copyright, Government of Ontario
1 Digital copy created for preservation and access purposes.  Access restricted.  For further details contact ascproj@yorku.ca
69 Digital copy created for preservation and access purposes.  Available by request for research purposes only.  All other uses must be cleared by patron through copyright holders.  For further details contact ascproj@yorku.ca
40 Digital copy created for preservation and access purposes. For further copyright information contact : ascproj@yorku.ca
5 Digital copy created for preservation and access purposes. Online streaming copy made available for research and non-commercial purposes only by creator. For further details contact ascproj@yorku.ca
101 Digitized for access and research purposes only. For further copyright information contact: ascproj@yorku.ca.
1 Edith Butler: contacted, permission pending receipt of official documents.
1 Enoch Kent contacted, permission granted. [date]. Songwriter : Public domain.
1 Enoch Kent: Contacted, permission granted.
15 For further copyright information contact : ASCproj@yorku.ca
22600 For further copyright information contact : ascproj@yorku.ca
1 For further copyright information contact : ascproj@yorku.ca||Taber Dulmage and Feheley
1 For further copyright information contact : ascproj@yorkuca
2 ILO
1 If credit is given and Crown copyright is acknowledged, the materials may be reproduced for non-commercial purposes. The materials may only be reproduced for commercial purposes under a licence from the Queen's Printer.
87 Item digitized for access and research purposes only. Copyright retained by Robert S. Mendelsohn Estate. For all other uses, contact archives@yorku.ca.
1 Ken Whiteley: contacted, permission granted.  Chris Whiteley permission granted. Sloth Band: two members contacted, permission granted. Third member deceased. John Davis : not contacted.
1 Lois Lilienstein: contacted, permission granted (pending receipt of official documents). Chris Whiteley: contact, permission granted. Rich Avery: contacted, no response as of 08.04.10. Dick Smith: contact info not yet found.
1 Malvina Reynolds: estate contacted twice, no response as of 30.03.2010.
1 Malvina Reynolds: estate contacted twice, no response as of 30.03.2010. Rosalie Sorrels: contact info not yet found.
1 Malvina Reynolds: estate contacted twice, no response as of 30.03.2010. Vera Johnson: estate contacted, permission granted.
3 Margaret Christl : contacted and permission granted.
1 Margaret Pierce: seeking contact information.
1 Michael Cooney contacted and permission granted.
1 Michael Cooney contacted and permission granted.  Songwriter : unknown, probably public domain.
1 Ming Wong: contacted, permission granted. Ming Chan: contacted, permission granted. Janet Chan: contacted, permission granted.
1 Murray McLauchlan: contacted twice, no response as of 27.04.2010.
2 NRTEE
1 Owen McBride contacted, permission granted.
1 Owen McBride contacted, permission granted.
1 Pat Byrne: contacted, permission granted.
1 Pembina Institute
91 Photograph now in public domain. For citation information or to obtain high resolution image, contact ascproj@yorku.ca or see Toronto Telegram FAQ.
1 Reproduced by permission of Professor R. Markey, July 2015.
1 Reproduced by permission.
1 Reproduced with permission of Environment Canada.
1 Reproduced with permission of Greenpeace Canada, July 2016.
1 Reproduced with permission of Unifor
2 Reproduced with permission of Unifor, July 2016.
1 Reproduced with permission of the Labor Network for Sustainability, July 2016.
1 Reproduced with permission of the government of Manitoba
1 Robbie MacNeill: contact info not yet found.
1 These materials may be reproduced in whole or in part without  charge or written permission, provided that appropriate source  acknowledgements are made and that no changes are made to  the contents. All other rights are reserved.
1 These works may be reproduced for non-commercial purposes if credit is given and Crown copyright is acknowledged.   These works may not be reproduced, in all or in part, for any commercial purpose except under a license from the Queen's Printer for Ontario. For information on reproducing Government of Ontario works, please contact ServiceOntario Publications at copyright@ontario.ca.
2 This document is protected by Crown copyright which is held by the Queen's Printer for Ontario. If credit is given and Crown copyright is acknowledged, the materials may be reproduced for non-commercial purposes.
1 This publication may be reproduced in whole or in part and in any form for educational and non-profit purposes without special permission from the copyright holder, provided that acknowledgement of the source is made. UNEP would appreciate receiving a copy of any publication that uses this material as a source.
1 Tommy Makem : Conor Makem contacted, permission granted.
1 Tony Barrand: contacted, no response as of 27.04.2010.
754 Use of this public-domain resource is unrestricted.
33 Use of this resource is governed by the terms and conditions of the Creative Commons "Attribution" License (http://creativecommons.org/licenses/by/2.0/)
3 Use of this resource is governed by the terms and conditions of the Creative Commons "Attribution-NonCommercial-NoDerivs 2.5" Canada http://creativecommons.org/licenses/by-nc-nd/2.5/ca/
2 copyright remains with the creator
1 medium, is hereby permitted provided that the reproduction is accurate and is not presented as official."
9 null
1 © Her Majesty the Queen in Right of Canada, represented by the Minister of the Environment.
1 © QUEST – Quality Urban Energy Systems of  Tomorrow
2 © Queen's Printer for Ontario
1 © Queen's Printer for Ontario. This document is protected by Crown copyright which is held by the Queen's Printer for Ontario.
22 © This Work is protected by copyright and made available for personal or public non-commercial use and may be reproduced, in part or in whole, and by any means, and may be further distributed for non-commercial use, without charge or further permission. All users are required to indicate that the reproduction, in part or in whole, is a copy of a Work of the National Round Table on the Environment and the Economy (NRTEE). Reproduction, in whole or in part, of this Work for the purpose of commercial redistribution is strictly prohibited. Furthermore, no right to modify or alter in any manner the Work is hereby granted.
5 © This Work is protected by copyright and made available for personal or public non-commercial use and may be reproduced, in part or in whole, and by any means, and may be further distributed for non-commercial use, without charge or further permission. All users are required to indicate that the reproduction, whether in part or in whole, is a copy of a Work of the National Round Table on the Environment and the Economy (NRTEE). Reproduction, in whole or in part, of this Work for the purpose of commercial redistribution is strictly prohibited. Furthermore, no right to modify or alter in any manner the Work is hereby granted.
1 ©National Round Table on the Environment and the Economy (NRTEE)
```

III. Digital Collections Metadata Enhancements
==============================================

- Normalization
    - Dates
    - Names
    - Rights?
- Clean-up
- Field Merging
    - Fields missing MODS context nodes
- Additions
- Coordinating & Documenting Updating Work
- How to perform this work (OpenRefine)

IV. Converting XML-based Metadata to RDF
========================================

- What does MODS in RDF mean?
- What does our repository Object describe?
- Context classes?
- External Systems linking?
- Mapping and conversion notes?
- How to convert and a sample of the RDF conversion


V. Supporting a RDF Ecosystem for Digital Collections
=====================================================

- Managing Entities (Context Classes, Authorities)
- Performing, judging, managing reconciliation
- Pushing/Pulling Updates across Systems
- Discovery System(s) Mappings


VI. Conclusions & Steps Forward
===============================

