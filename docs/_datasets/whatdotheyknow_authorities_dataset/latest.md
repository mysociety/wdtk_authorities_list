---
name: whatdotheyknow_authorities_dataset
title: WhatDoTheyKnow Authorities Dataset
description: "Dataset of UK public authorities and tags that powers WhatDoTheyKnow\n"
version: latest
keywords:
- United Kingdom
- Groups & Bodies
- WhatDoTheyKnow
licenses:
- name: CC-BY-SA-4.0
  path: https://creativecommons.org/licenses/by-sa/4.0/
  title: Creative Commons Attribution-ShareAlike 4.0 International License
contributors:
- title: WhatDoTheyKnow Volunteers
  path: https://whatdotheyknow.com
  role: author
- title: mySociety
  path: https://mysociety.org
  role: author
custom:
  build: wdtk_authorities_list.build:build
  tests:
  - test_whatdotheyknow_authorities_dataset
  dataset_order: 0
  download_options:
    gate: default
    survey: default
    header_text: default
  composite:
    xlsx:
      include: all
      exclude: none
      render: true
    sqlite:
      include: all
      exclude: none
      render: true
    json:
      include: all
      exclude: none
      render: false
  change_log:
    0.73.0: Changed render type to static - no individual version updates
  datasette:
    about: Info & Downloads
    about_url: https://pages.mysociety.org/wdtk_authorities_list/datasets/whatdotheyknow_authorities_dataset/0_73_0
  formats:
    csv: true
    parquet: true
resources:
- title: Public Authorities
  description: WhatDoTheyKnow's list of UK public authorities
  custom:
    row_count: 46950
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/wdtk_authorities_list/datasets/whatdotheyknow_authorities_dataset/0_73_0#authorities
  path: authorities.csv
  name: authorities
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: iso8859-1
  schema:
    fields:
    - name: version
      type: integer
      description: The current version of this authority's entry in this dataset
      constraints:
        unique: false
      example: 1
    - name: internal-id
      type: integer
      description: Internal WDTK ID
      constraints:
        unique: true
      example: 3
    - name: name
      type: string
      description: Name of the authority
      constraints:
        unique: true
      example: 101 Medical Practice, Troon
    - name: short-name
      type: string
      description: Short name of the authority
      constraints:
        unique: false
      example: 2013 WPFG
    - name: url-name
      type: string
      description: WhatDoTheyKnow's URL name for the authority
      constraints:
        unique: true
      example: 101_medical_practice_troon
    - name: tags
      type: string
      description: "A list of tags that describe the authority. Pipe seperated.\n"
      constraints:
        unique: false
      example: 16_plus|Academy_16-19_converter|Greenwich|academies|charity:exempt|exempt_charity|not_many_requests|school|school_new_nov2020|urn:138966
    - name: home-page
      type: string
      description: The home page of the authority.
      constraints:
        unique: false
      example: http://207dentalcare.com/
    - name: publication-scheme
      type: string
      description: The publication scheme used by the authority
      constraints:
        unique: false
      example: http://about.edinburghleisure.co.uk/freedom-of-information/guide-to-information/
    - name: disclosure-log
      type: string
      description: URL for the disclosure log of the authority
      constraints:
        unique: false
      example: http://about.edinburghleisure.co.uk/freedom-of-information/disclosure-logs/
    - name: notes
      type: string
      description: WDTK's notes for this authority
      constraints:
        unique: false
      example: "\n\n\r\nThis body has been replaced by the Keeping Bristol Safe Partnership.\n\
        \n\r\n\r\nThe core membership of Local Safeguarding Children Boards ws set\
        \ out in the Children Act 2004, and includes Local Authorities, health bodies,\
        \ the police and others. Whilst LSCBs were not generally subject to the Freedom\
        \ of Information Act 2000 they were included on this site due to their public\
        \ functions."
    - name: created-at
      type: string
      description: Date the authority's entry was created in this dataset
      constraints:
        unique: false
      example: 2007-12-14 01:57:33 +0000
    - name: updated-at
      type: string
      description: Date the authority's entry was last updated in this dataset
      constraints:
        unique: false
      example: 2013-09-24 12:00:27 +0100
    - name: defunct
      type: boolean
      description: A boolean indicating whether the authority is defunct
      constraints:
        unique: false
        enum:
        - false
        - true
      example: 'False'
    - name: categories
      type: string
      description: "A list of categories that the authority belongs to. Pipe seperated.\n"
      constraints:
        unique: false
      example: Academic Health Science Networks|Companies limited by guarantee|Limited
        companies|NHS bodies
    - name: top-level-categories
      type: string
      description: "A list of top-level categories that the authority belongs to.\
        \ Pipe seperated.\n"
      constraints:
        unique: false
      example: By legal form/status
    - name: single-top-level-category
      type: string
      description: A single top-level category, automatically chosen from the list
        of top-level categories for quick lookups.
      constraints:
        unique: false
      example: Education
  hash: b9fac2621631c0bc04e58c816d52568d
- title: Categories
  description: Lookup between a category name, category header, and top-level category
    of a public authority.
  custom:
    row_count: 289
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/wdtk_authorities_list/datasets/whatdotheyknow_authorities_dataset/0_73_0#authorities_categories
  path: authorities_categories.csv
  name: authorities_categories
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: category-tag
      type: string
      description: A tag that describes a set of authorities.
      constraints:
        unique: true
      example: ACJPS
    - name: top-level-category
      type: string
      description: A top-level category of the authorities in the category. Can be
        multiple, pipe-seperated.
      constraints:
        unique: false
      example: By legal form/status
    - name: category-name
      type: string
      description: The name of a category that describes a set of categories.
      constraints:
        unique: true
      example: Academic Health Science Networks
  hash: 158c732e3e10d7269317d0d64b09ad72
- title: Public authority ID lookup
  description: Lookup between a public authority WDTK url and its ID in various ID
    schemas
  custom:
    row_count: 84448
    datasette:
      about: Info & Downloads
      about_url: https://pages.mysociety.org/wdtk_authorities_list/datasets/whatdotheyknow_authorities_dataset/0_73_0#authorities_id_lookup
  path: authorities_id_lookup.csv
  name: authorities_id_lookup
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: schema
      type: string
      description: The ID schema this ID belongs to
      constraints:
        unique: false
      example: CSP21CD
    - name: id
      type: string
      description: The ID in the specified schema
      constraints:
        unique: false
      example: '00008894'
    - name: wdtk-url-name
      type: string
      description: The WDTK URL name of the authority
      constraints:
        unique: false
      example: 131_dental_rotherham
  hash: 7e769b29816e045a082b15372d72ba24
full_version: 0.73.0
permalink: /datasets/whatdotheyknow_authorities_dataset/latest
---
