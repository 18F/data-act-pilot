###Purpose

This will be a living doc outlining our current thoughts on the process and workflow of reporting agencies and Treasury regarding data unification, mapping, and validation.

####Assumptions and suggestions

For the sake of the pilot that 18F is currently involved in developing, we can make certain assumptions and decisions around how the data can be delivered to Treasury by the reporting agencies. Ultimately, these decisions lie with Treasury and the group responsible for developing the final ingestion and validation tools, but for now we can make certain suggestions regarding the data format and validation:

1. We suggest that those responsible for implementing the Data Act provide a simple, CSV based output format implementing the Data Act schema. Agencies should be able to map their existing data to this format prior to submission to Treasury. This format should require the joining of financial and award level data.

2. There should be a single CSV file for each type of award (grant, loan, etc). Though many of the data elements will be shared across award types, there is enough variance in how they are used (not to mention several award-type-specific fields), that for ease of validation we suggest that individual files should be provided.

3. We suggest that a validation tool should be made available to the reporting agencies. This tool could be applied to data represented in the csv format described above to do most validation prior to submission to Treasury. This should serve to assist agencies in making sure their data is correctly represented, and decrease the number of failed submissions.

4. Finally, after submission, Treasury should perform a secondary validation which would include all of the validation rules run by the aforementioned tool (to provide a sanity check), as well as any validations required against third party, authoritative sources (to be determined).

####Proposed workflow

![Workflow diagram](updated-validation-flow.png)

####Input files

Per the decision points above, we're proposing that agencies submit the following types of csv files as part of their DATA Act submission. Note that some file types may not be applicable to all agencies.

Note that the required fields included below will be revised once the DATA Act schema is finalized.

**Common Fields**

*Financial Account Information*
* Treasury Account Symbol (TAS)
    * sub-level prefix
    * allocation transfer agency ID
    * beginning period of availability
    * ending period of availability
    * availability type code
    * main Account
    * sub Account
    * as of time
    * Account
* Object Class
* Amount of Budget Authority Appropriated
* Amount of Other Budgetary Resources
* Obligated Amount
* Unobligated Amount
* Program Activity
* Outlay

*Award Amount Information*
* Funding Action Obligation
* Non-Federal Funding Amount
* Current Total Funding Obligation Amount on Award
* Current Total Value of Award
* Potential Total Value of Award

*Awardee Information*
* Awardee/Recipient Legal Business Name
* Awardee/Recipient Legal Business DUNS Number
* Awardee/Recipient Legal Business DUNS+4 Number
* Entity ID (unique identifier that may be consistently applied government-wide)
* Global Awardee/Recipient Parent DUNS Number
* Global Awardee/Recipient Parent Legal Business Name
* Awardee/Recipient Legal Business Street Address Line 1
* Awardee/Recipient Legal Business Street Address Line 2
* Awardee/Recipient Legal Business Street Address Line 3
* Awardee/Recipient Legal Business City
* Awardee/Recipient State
* Awardee/Recipient Legal Business  US Zip Code +4
* Awardee/Recipient Postal Code
* Awardee/Recipient Legal Business Congressional District
* Awardee/Recipient Legal Business Country Code
* Awardee/Recipient Legal Business Country Name

*Award Characteristic Information*
* Award Number
* Award ID (unique identifier that may be consistently applied government-wide)
* Type of Transaction Code
* Component Treasury Account Symbol
* Award Description
* Modification/Amendment Number
* Parent Award Number
* Action Date
* Primary Place of Performance City
* Primary Place of Performance State
* Primary Place of Performance County Name
* Primary Place of Performance County Code
* Primary Place of Performance Zip Code +4
* Primary Place of Performance Congressional District
* Primary Place of Performance Country Code
* Primary Place of Performance Country Name
* Record Type
* Type of Action
* Recipient Type/Business Type

*Funding Entity Information*
* Funding Agency Name
* Funding Agency Code
* Funding Sub Tier  Agency Name
* Funding Sub Tier  Agency Code
* Funding Office Name
* Funding Office Code

*Awarding Entity Information*
* Awarding Agency Name
* Awarding Agency Code
* Awarding Sub Tier Agency Name
* Awarding Sub Tier Agency Code
* Awarding Office Name
* Awarding Office Code

**Grants and Payments to Individuals**
The grants and payments to individuals file will include the common fields above and the following:
* CFDA Program Number
* CFDA Program Title

**Contracts**
The contracts file will include the common fields above and the following:
* Highly Compensated Officer #1 First Name
* Highly Compensated Officer #1 Last Name
* Highly Compensated Officer #2 First Name
* Highly Compensated Officer #2 Last Name
* Highly Compensated Officer #3 First Name
* Highly Compensated Officer #3 Last Name
* Highly Compensated Officer #4 First Name
* Highly Compensated Officer #4 Last Name
* Highly Compensated Officer #5 First Name
* Highly Compensated Officer #5 Last Name
Highly Compensated Officer #1 Total Compensation
* Highly Compensated Officer #2 Total Compensation
* Highly Compensated Officer #3 Total Compensation
* Highly Compensated Officer #4 Total Compensation
* Highly Compensated Officer #5 Total Compensation
* NAICS Code
* NAICS Description

**Loans**
The loans file will include the common fields above and the following:

* ??

**Insurance**
The insurance file will include the common fields above and the following:

* ??

####Validation rules

Proposed rules are being documented at [sba-business-rules.md](sba-business-rules.md).

####Validation script

An initial stab at a validator can be found at [processors/validator.py](processors/validator.py). Rules are added as simple python objects, but could be pulled out of the script and parsed at runtime.
