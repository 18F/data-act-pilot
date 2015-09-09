## Background

The Digital Accountability and Transparency Act (DATA Act) became law in May, 2014. Among other things, the law mandates government-wide standards for financial data and calls for improved quality of data submitted to [USAspending.gov](https://usaspending.gov "USAspending.gov").

Unsurprisingly, implementation of the DATA Act is a large amount of work with many moving pieces. One such piece is developing the financial data standard, and a component of that is testing the standard with real agency data.

Thus, this project is an exploration of the DATA Act data submission process from the agency perspective. The repository is learning-in-progress, subject to change, and its goal is to clarify the steps and tools agencies will need as they undertake DATA Act compliance.

Thanks to the Small Business Administration for leading the way and lending their time and expertise to this effort.

## Overview

Below is the current DATA Act submission process used by this prototype.

![DATA Act Pilot Process Flow](https://raw.githubusercontent.com/18F/data-act-pilot/master/SBA%20pilot%20process.png)

## Glossary

A few terms you might see floating around:

* **JAAMS**: SBA's financial system
* **Prism**: SBA's grants and contracts system
* **SAM**: Federal government-wide system that contains information about entities (businesses, individuals, or government agencies) that do business with the federal government. SAM stands for _System for Award Management_.
* **DATA Act Schema (_Schema_)**: The generic model of the relationships between the data elements that agencies must report to Treasury as part of the DATA Act and previous transparency legislation.

## Resources
Here's a list of DATA Act resources and artifacts that might be useful to people working on this pilot:

* [Finalized data element definitions](https://max.gov/maxportal/assets/public/offm/DataStandardsFinal.htm "Finalized Data Act Element Definitions").
* [SBA Entity Relationship Diagram](https://raw.githubusercontent.com/18F/data-act-pilot/master/assets/images/jaams-prism-data-act-mapping.png "SBA ERD"). A diagram of the relationships between the JAAMS and Prism tables that contain the fields being mapped to the DATA Act schema.
* [Research Questions](https://github.com/18F/data-act-pilot/labels/research%20questions "open issues labeled as 'research'"). Questions (and some answers) that have emerged during the pilot. Closed (_i.e._, answered) questions are [here](https://github.com/18F/data-act-pilot/issues?q=label%3A%22research+questions%22+is%3Aclosed "closed issues labeled as 'research'").
* [DATA Act Playbook](https://www.usaspending.gov/Documents/Summary%20of%20DATA%20Act%20Playbook.pdf "DATA Act Playbook"). Recommended steps for agencies to fulfill DATA Act requirements.
* Pilot Screencast:
    * [Mac and newer versions of Windows](assets/screencast/data_act_pilot_screencast_sept_2015.mp4 "Pilot screencast, .mp4 version")
    * [Older versions of Windows](assets/screencast/data_act_pilot_screencast_sept_2015.mp4 "Pilot screencast, .avi version")

## Data

This prototype explores the process for submitting DATA Act data to Treasury. Thus, it is tightly scoped and doesn't strive to answer every question or address every edge case.

We developed the prototype using one year of SBA grants data (fiscal year 2014).
