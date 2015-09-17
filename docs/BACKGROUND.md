## Background
The Digital Accountability and Transparency Act (DATA Act) became law in 2014. Among other things, the act mandates government-wide standards for financial data. It also calls for improved quality of data submitted to [USAspending.gov](https://usaspending.gov "USAspending.gov").

Implementation of the DATA Act requires substantial work and has many moving pieces. This project delves into one of those pieces –  developing a financial data standard and a component to test that standard with real agency data.

Thanks to the Small Business Administration (SBA) for leading the way and lending their time and expertise to this effort.

## Overview
This project explores data submission from the agency perspective. This repository aims to clarify the steps and tools agencies need as they undertake DATA Act compliance. Please note: This is a work in progress and subject to change. 

Below is the current DATA Act submission process used by this prototype.

![DATA Act pilot process flow](https://raw.githubusercontent.com/18F/data-act-pilot/master/SBA%20pilot%20process.png)

## Glossary
A few terms you might encounter:

* **JAAMS**: SBA's financial system
* **Prism**: SBA's grants and contracts system
* **SAM**: _System for Award Management_, a federal, government-wide system that contains information about entities (businesses, individuals, or government agencies) that do business with the federal government
* **DATA Act Schema (_Schema_)**: the generic model of the relationships between the data elements that agencies must report to Treasury as part of the DATA Act and previous transparency legislation

## Resources
Below, we've identified some useful resources and artifacts for people working on this pilot.

* The OMB published [finalized data element definitions](https://max.gov/maxportal/assets/public/offm/DataStandardsFinal.htm "Finalized Data Act Element Definitions").
* Mapping document: This is the document that maps specific SBA JAAMS and Prism attributes to their DATA Act schema counterparts. It's not currently public and resides in the data folder.
* The [SBA entity relationship diagram](https://raw.githubusercontent.com/18F/data-act-pilot/master/assets/images/jaams-prism-data-act-mapping.png "SBA ERD") shows the relationships between the JAAMS and Prism tables that contain the fields being mapped to the DATA Act schema.
* Explore [research questions](https://github.com/18F/data-act-pilot/labels/research%20questions "open issues labeled as 'research'") (and some answers) that have emerged during the pilot. Answered questions are [stored as "closed" in GitHub](https://github.com/18F/data-act-pilot/issues?q=label%3A%22research+questions%22+is%3Aclosed "closed issues labeled as 'research'").
* The [DATA Act Playbook](https://www.usaspending.gov/Documents/Summary%20of%20DATA%20Act%20Playbook.pdf "DATA Act Playbook") contains recommended steps for agencies to fulfill DATA Act requirements.
* Pilot screencast:
    * [Mac and newer versions of Windows](screencasts/data_act_pilot_screencast_sept_2015.mp4 "Pilot screencast, .mp4 version")
    * [Older versions of Windows](screencasts/data_act_pilot_screencast_sept_2015.avi "Pilot screencast, .avi version")

## Data
This prototype explores the process for submitting DATA Act data to Treasury. Thus, it's tightly scoped and doesn't strive to answer every question or address every edge case.

We developed the prototype using one year of SBA grants data (fiscal year 2014).
