# York University Libraries Metadata Summit
### November 3-4

## This Repository

Contains links, guides, scripts, and datasets for analysis of York University Library Digital Collections.

## Running Assessment scripts

_Should_ work with python 2 and python 3 (tested with python 3.5). Run in top level of this directory.

Run `pip install -r requirements.txt` first to download all needed python libraries.

### York Digital Collections Islandora

**Generate full output from local MODS/XML files copy**

```bash
python scripts/file_modsAnalysis.py MODS_data/yudl_mods/20161030/all/
```

**Generate full output from calling Islandora PIDs (will take a while, requires text file with list of PIDs)**

```bash
python scripts/pid_modsAnalysis.py MODS_data/yudl_mods/20161030/yul:123929.txt
```

**Get all unique field values for the given XPath**

```bash
python scripts/file_modsAnalysis.py MODS_data/yudl_mods/20161030/all/ -x 'mods:subject/mods:topic' | sort | uniq -c   
```

### YorkSpace DSpace

**Generate full output**

```bash
python scripts/dim_analysis.py DIMS_data/yorkspace.dims.xml
```

**Get all unique values for the given XPath that queries DIMS/XML**

```bash
python scripts/dim_analysis.py DIMS_data/yorkspace.dims.xml -x 'dim:field[@element="identifier"]' | sort | uniq -c      
```

## York University Library Digital Collections Overall Assessment

```

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


```

## YorkSpace Overall Assessment

```
            dc:contributor: |                         |     19/29561 |   0%
    dc:contributor.advisor: |=                        |   1368/29561 |   4%
     dc:contributor.author: |================         |  19617/29561 |  66%
     dc:contributor.editor: |                         |      4/29561 |   0%
      dc:contributor.other: |                         |      1/29561 |   0%
          dc:coverage.city: |===                      |   3995/29561 |  13%
        dc:coverage.county: |===                      |   3995/29561 |  13%
        dc:coverage.region: |===                      |   3884/29561 |  13%
             dc:coverage.x: |===                      |   3995/29561 |  13%
             dc:coverage.y: |===                      |   3995/29561 |  13%
                dc:creator: |=======                  |   8583/29561 |  29%
                   dc:date: |==========               |  11937/29561 |  40%
       dc:date.accessioned: |======================== |  29559/29561 |  99%
         dc:date.available: |======================== |  29557/29561 |  99%
         dc:date.copyright: |=                        |   1261/29561 |   4%
           dc:date.created: |================         |  19013/29561 |  64%
            dc:date.issued: |======================== |  29303/29561 |  99%
           dc:date.updated: |====                     |   5337/29561 |  18%
      dc:degree.discipline: |=                        |   1267/29561 |   4%
         dc:degree.grantor: |                         |      3/29561 |   0%
           dc:degree.level: |=                        |   1267/29561 |   4%
            dc:degree.name: |=                        |   1263/29561 |   4%
            dc:description: |=====================    |  24851/29561 |  84%
   dc:description.abstract: |===                      |   4400/29561 |  14%
      dc:description.local: |===                      |   3996/29561 |  13%
 dc:description.provenance: |=========================|  29561/29561 | 100%
dc:description.sponsorship: |=                        |   1258/29561 |   4%
                 dc:format: |=====================    |  25010/29561 |  84%
          dc:format.extent: |                         |    231/29561 |   0%
        dc:format.mimetype: |                         |    231/29561 |   0%
             dc:identifier: |=====================    |  25498/29561 |  86%
    dc:identifier.citation: |================         |  19868/29561 |  67%
        dc:identifier.isbn: |                         |    311/29561 |   1%
        dc:identifier.issn: |                         |    454/29561 |   1%
       dc:identifier.other: |==                       |   3470/29561 |  11%
         dc:identifier.uri: |=========================|  29561/29561 | 100%
               dc:language: |                         |     21/29561 |   0%
           dc:language.iso: |=========                |  10649/29561 |  36%
              dc:publisher: |=======                  |   9349/29561 |  31%
               dc:relation: |==========               |  12650/29561 |  42%
    dc:relation.isformatof: |========                 |  10549/29561 |  35%
      dc:relation.ispartof: |==============           |  17471/29561 |  59%
dc:relation.ispartofseries: |=====================    |  25087/29561 |  84%
       dc:relation.mapsuri: |===                      |   3995/29561 |  13%
      dc:relation.replaces: |                         |    978/29561 |   3%
           dc:relation.uri: |                         |   1057/29561 |   3%
                 dc:rights: |======================   |  26119/29561 |  88%
         dc:rights.article: |                         |    657/29561 |   2%
         dc:rights.journal: |                         |    630/29561 |   2%
       dc:rights.publisher: |                         |    557/29561 |   1%
             dc:rights.uri: |=====                    |   6066/29561 |  20%
                dc:subject: |========                 |  10210/29561 |  34%
 dc:subject.classification: |                         |      1/29561 |   0%
       dc:subject.keywords: |=                        |   1282/29561 |   4%
           dc:subject.lcsh: |                         |      1/29561 |   0%
                  dc:title: |======================== |  29559/29561 |  99%
      dc:title.alternative: |=                        |   1801/29561 |   6%
                   dc:type: |=======================  |  28299/29561 |  95% ``

