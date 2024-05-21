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
    row_count: 46544
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
      example: "\n\n\r\nGreat British Railways is to be a public body responsible\
        \ for integrating the railways and delivering passenger-focused travel with\
        \ simpler, modern fares and reliable services.*\n\n\r\nA company called Great\
        \ British Railways Transition Team already exists and has been charged with\
        \ the responsibility, among other things, of \"creating\" Great British Railways.\
        \ Unfortunately, we don't have a working email address for this authority.\n\
        \nIf you would like to help us out, just do a little bit of research to find\
        \ the correct address, click on the \"Ask us to update FOI email\" link, and\
        \ fill out the details.  Remember to put details of the source of the email\
        \ in the source URL/notes box. \n\nTop tip: try looking for Freedom of Information\
        \ policies or Publication Schemes, otherwise, just use a generic contact email\
        \ address.\n\nIf you manage to find one, if you prefer, you can also let us\
        \ know by contacting us.\n\nPlease ignore this note if it appears on a page\
        \ that redirects readers to other bodies (a signpost page).  Coming soonThis\
        \ is a placeholder page created before this public body came into existence.\
        \ If this body is now up and running please contact us and let us know! "
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
  hash: 55aa7748593ba2e42f2e78cc3f601d79
- title: Categories
  description: Lookup between a category name, category header, and top-level category
    of a public authority.
  custom:
    row_count: 287
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
  hash: 63e27ab3c58ed5b5bf4d0ce2f85788a3
- title: Public authority ID lookup
  description: Lookup between a public authority WDTK url and its ID in various ID
    schemas
  custom:
    row_count: 84092
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
      example: Charity
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
  hash: 41b383dfd35fa2ae7eda9e5231bdec6c
full_version: 0.73.0
permalink: /datasets/whatdotheyknow_authorities_dataset/latest
---
