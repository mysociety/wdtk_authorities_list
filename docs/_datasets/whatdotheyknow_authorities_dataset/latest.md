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
    row_count: 46507
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
      example: "\r\n<div id=\"request_status\" class=\"request-status-message request-status-message--error_message\"\
        >\r\n<h3><i class=\"icon-standalone icon_error_message\"></I> This authority\
        \ no longer exists</h3>\r\n<p>This organisation has transferred its housing\
        \ stock to an alternative organisation, and no longer exists.\r\n<sup>[<a\
        \ href=\"https://web.archive.org/web/20231204132949/https://www.blackwoodgroup.org.uk/latest-news/abbeyfield-scotland-joins-blackwood-homes-care-2523/\"\
        \ title=\"Information about the transfer from Abbeyfield, on the Blackwood\
        \ website (opens in a new tab)\" target=\"_blank\">1</a>, \r\n <a href=\"\
        https://web.archive.org/web/20231204133147/https://www.housingregulator.gov.scot/about-us/news/weve-completed-the-de-registration-of-abbeyfield-scotland-ltd\"\
        \ title=\"De-registration confirmation on the Scottish Housing Regulator website\
        \ (opens in a new tab)\" target=\"_blank\">2</a>]</sup>.</p>\r\n<h3><i class=\"\
        icon-standalone icon_successful\"></I> Looking to make a new request?</h3>\r\
        \n<p>You can make a request to Blackwood Homes and Care <b><a href=\"/body/blackwood_homes_and_care\"\
        >by clicking here</a></b>.</p>\r\n</div> <p>This body is a <abbr title=\"\
        sometimes also referred to as a Housing Association\">Registered Social Landlord</abbr>\
        \ (RSL), in Scotland.</p>\r\n\r\n<p>RSLs became subject to transparency legislation\
        \ in November 2019, after they were <a href=\"https://www.itspublicknowledge.info/registered-social-landlords\"\
        \ title=\"Find out more about designation on the Scottish Information Commissioner's\
        \ website (opens in a new tab)\" target=\"_blank\">'designated' by the Scottish\
        \ Ministers</a>. RSLs are subject to FOI legislation for activities relating\
        \ to the management of social housing and <abbr title=\"A Scottish RSL is\
        \ subject to FOI law in relation to any activity relating to (1) the management\
        \ of social housing accommodation, (2) the prevention and alleviation of homelessness,\
        \ (3) the provision and management of sites for gypsies and travellers and\
        \ (4) supplying information to the Scottish Housing Regulator in relation\
        \ to the RSLs financial well-being and standards of governance. RSLs are not\
        \ subject to FOI law for activities relating to property factoring. Property\
        \ factoring means looking after the shared parts of land or buildings owned\
        \ by more than one person such as the stairs and corridors.\">certain other\
        \ activities</abbr/>.\r\n</p>\r\n<hr>\r\n<h3>Need help with housing issues?</h3>\r\
        \n<p>You can't use our service to ask for help with housing issues or for\
        \ customer service enquiries (<a href=\"https://www.whatdotheyknow.com/help/requesting#data_protection\"\
        \ alt=\"find out why\">find out why</a>).\r\n</p>\r\n<p>\r\nIf you need help\
        \ with a problem, <a href=\"https://www.citizensadvice.org.uk/scotland/housing/\"\
        \ title=\"Information about housing on the Citizens Advice Scotland website\
        \ (opens in a new tab)\" target=\"_blank\">Citizens Advice Scotland</a>, and\
        \ <a href=\"https://scotland.shelter.org.uk\" target=\"_blank\" title=\"Shelter\
        \ Scotland (opens in a new tab)\">Shelter Scotland</a>, might be able to help.\
        \ The Scottish Housing Regulator also have <a href=\"https://www.housingregulator.gov.scot/for-tenants\"\
        \ title=\"Information for tenants on the Scottish Housing Regulator website\
        \ (opens in a new tab)\" target=\"_blank\">information for tenants on their\
        \ website</a> which you might find useful.\r\n<br /><br />You might also be\
        \ able to ask your local <abbr title=\"elected members, such as your local\
        \ Councillor, MSP, or MP\">elected members</abbr> for help. Find out more\
        \ on the <a href=\"https://www.writetothem.com\">WriteToThem</a> website.\r\
        \n</p>\r\n<hr>\r\n<div class=\"request-status-message request-status-message--rejected\"\
        ><h3>Looking for information about yourself?</h3>\r\n<p>⛔️ You can't ask for\
        \ information about yourself using our service – <a href=\"https://www.whatdotheyknow.com/help/requesting#data_protection\"\
        \ title=\"Find out why you cannot ask for personal information using WhatDoTheyKnow,\
        \ and what to do\">find out why</a>.</p></div>"
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
  hash: 64c94d2bc15e114ddced4c9882e5de7c
- title: Categories
  description: Lookup between a category name, category header, and top-level category
    of a public authority.
  custom:
    row_count: 284
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
  hash: 2223800fb36b019bdf7f67be3394860d
- title: Public authority ID lookup
  description: Lookup between a public authority WDTK url and its ID in various ID
    schemas
  custom:
    row_count: 84082
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
  hash: b2f3e34adf40289dbad1109032379af8
full_version: 0.73.0
permalink: /datasets/whatdotheyknow_authorities_dataset/latest
---
