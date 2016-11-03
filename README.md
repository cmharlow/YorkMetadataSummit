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

## YorkSpace Assessment

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

