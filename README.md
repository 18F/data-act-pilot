# DATA Act Pilot

This repository contains code for a Small Business Administration pilot project that:
* maps agency financial and award data to DATA Act elements,
* translates them to a uniform DATA Act format, and
* validates the results.

This work is a small experiment using real agency data. The diagrams and other artifacts here do not represent official DATA Act guidance or policy, and the code does not represent an official DATA Act product.

## Background

This project is an exploration of the DATA Act data submission process from the agency perspective. The repository is learning-in-progress, subject to change, and its goal is to clarify the steps and tools agencies will need as they undertake DATA Act compliance.

Thanks to the Small Business Administration for leading the way and lending their time and expertise to this effort.

### Questions?

Because this is a small experiment and a tiny piece of the overall DATA Act implementation, 18F is unable to speak with vendors individually about the work. We welcome the DATA Act community to follow the project and contribute here.

## Overview

Progress and upcoming work are viewable on our Github/Waffle-based task board: https://waffle.io/18F/data-act-pilot

Below is an overview of the process.

![DATA Act Pilot Process Flow](https://raw.githubusercontent.com/18F/data-act-pilot/master/updated-validation-flow.png)

## Glossary
* **JAAMS**: SBA's financial system
* **Prism**: SBA's grants and contracts system
* **SAM**: Federal government-wide system that contains information about entities (businesses, individuals, or government agencies) that do business with the federal government. SAM stands for _System for Award Management_.
* **DATA Act Schema (_Schema_)**: The generic model of the relationships between the data elements that agencies must report to Treasury as part of the DATA Act and previous transparency legislation.

## Resources
Here's a list of DATA Act resources and artifacts that might be useful to people working on this pilot:

* [Finalized data element definitions](https://max.gov/maxportal/assets/public/offm/DataStandardsFinal.htm "Finalized Data Act Element Definitions").
* [In-progress data element definitions](http://fedspendingtransparency.github.io/dataelements/ "Collaboration Space: Federal Spending Data Elements"). For elements on this list that have been finalized, use the finalized version of the definition.
* Mapping document. This is the document that maps specific SBA JAAMS and Prism attributes to their DATA Act schema counterparts. It's not currently public and resides in the data folder.
* [SBA Entity Relationship Diagram](https://raw.githubusercontent.com/18F/data-act-pilot/master/assets/images/jaams-prism-data-act-mapping.png "SBA ERD"). A diagram of the relationships between the JAAMS and Prism tables that contain the fields being mapped to the DATA Act schema.
* [Research Questions](https://github.com/18F/data-act-pilot/labels/research%20questions "open issues labeled as 'research'"). Questions (and some answers) that have emerged during the pilot. Closed (_i.e._, answered) questions are [here](https://github.com/18F/data-act-pilot/issues?q=label%3A%22research+questions%22+is%3Aclosed "closed issues labeled as 'research'").
* [DATA Act Playbook](https://www.usaspending.gov/Documents/Summary%20of%20DATA%20Act%20Playbook.pdf "DATA Act Playbook"). Recommended steps for agencies to fulfill DATA Act requirements.

## Data
For the first iterations of this pilot, we're using SBA 2014 grants data.

Because it contains PII (personally identifiable information), the SBA data is not included in the code repository. The data includes:

* Extracts from JAAMS, SBA's financial system
* Extracts from Prism, SBA's awards system

These extracts will be supplemented by calls to the [SAM API](https://gsa.github.io/sam_api/sam/index.html), which contains details about entities (businesses and individuals) that receive federal funds.

### Data Structure
For reference, the data accessed in the code are structured as follows. The text files are extracts from their respective underlying databases and have been provided to the team in comma-quote delimited format.

* `data/jaams`: text file extracts from JAAMS
* `data/jaams/sql`: sql for JAAMS table creation/joins
* `data/prism`: text file extracts from Prism
* `data/prism/sql`: sql for Prism table creation/joins

### Running the Processors
These directions assume that the project is already installed on your system. If you don't have the project installed and running, please see [INSTALL.md](INSTALL.md "Installation instructions").

There are two steps for converting SBA data to DATA Act input format.

The first reads raw text files from SBA (JAAMS and Prism), joins the awards and financial data, and writes it to four standardized DATA Act files.

The second validates the four files against the pilot's working subset of business rules, found here: [sba-business-rules.md](sba-business-rules.md "SBA Business Rules").

Example usage (to run both processes):

`python processors/process_source.py -o data/data_act.csv`

`python processors/validattor [micah to fill in]`

### Querying the SAM api
The SAM data utility queries the SAM API based on DUNS number and returns a JSON version of the response. A list of requested fields can be supplied to limit the response to only the data required. A full list of available fields and their definitions can be found at [SAM Field Definitions](http://gsa.github.io/sam_api/sam/fields.html).

Example usage:

To get all fields for a given DUNS:

`python processors/get_sam_data.py 8291938660000`

To limit response to a list of fields:

`python processors/get_sam_data.py 8291938660000 --fields registrationDate legalBusinessName samAddress`
