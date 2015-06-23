##DATA Act Implementation Playbook Digest

OMB and Treasury are in the process of authoring an implementation playbook 8 step to outline a process for agencies to adapt their current financial and awards data to the DATA Act schema. This digest is to pull out key information from the playbook to help in the SBA DATA Act pilot, as well as document our process along side the 8 steps. *This document is subject to change.*

#### Approach: 
OMB and Treasury is taking an approach that is data-centric, incremental, maximizing existing processes, collaborative, and interative/agile.

####Agency Role in the implementation of the DATA Act: 
1. Plan and implement changes to systems: 
2. Map data from Agency Schema to DATA Act Schmea
3. Test DATA Act Schema data and submit. 


Implementation Checklist 

1. Organize team:
	- *Designate a Senior Accountable Official.* SAO is responsbile for their agency's implementation which includes overseeing the governance and progress of the workgroup.
	- *Form workgroup with subject matter experts (SMEs)* Members should come from all across the organization, such as budget, accounting, grants, procurement, loans, and information technology
	- *Once established the Workgroup creates road map and timeline for implementation* Determine milestons, set up group accountability ground rule, establish roles and reponsibilites for people and offices within your agency. 

2. Review Elements 
	- Read and review the [Data element definitions](http://fedspendingtransparency.github.io/dataelements/)
	- Provide feedback or ask clarifying questions to OMB and Treasury by emailing DATAPMO@fiscal.treasury.gov

3. Inventory Data
	-*Locate DATA Act elements in agency systems:* Identify and understand linkages and/or gaps in how DATA Act elements are captured in the financial and management award systems.  
	- Document systems, processes, and policies for each element
	- Brainstorm potential improvements to agency systems, processes, and policies

	--------
	- *For the SBA Pilot* here is the [draft template](inventory_mapping.csv) for mapping data elements to DATA Act schema

4. Design and Strategize
	- *Establish leads and/or integrated project teams*: Establish some leads and/or smaller integrated project teams that will work to develop solutions to fill each specific gap in agency data Workgroups may also want to identify key programs, offices, or business lines that could be leveraged to pilot specific aspects of agency implementation
	- *Plan to capture all DATA Act elements:* Develop options for addressing gaps in the completeness and accuracy of DATA Act elements. Also, consider how they can best leverage current systems, already scheduled system upgrades, and Federal Shared Service Providers.
	
	---------
	*For SBA pilot*
	- In this diagram it shows that data will be coming from two systems PRISM and JAAMS. 

	![Workflow diagram](../updated-validation-flow.png)

5. Mapping data to DATA-Act Schema
	- *Build "mapping engine" that populates DATA Act Schema with agency data:* Map data from the Agency Schema (original format) to the DATA Act Schema. This component should have the capability to link data from disparate systems and transform data into the required DATA Act Schema format. 

	---------
	*For SBA pilot* 

	- There are two processes that convert SBA data to DATA Act format.

		- The first reads raw text files from SBA (JAAMS and Prism) and combines them into a single file of awards+modifications (what the [draft schema](https://raw.githubusercontent.com/18F/data-act-pilot/master/schema/data-act-schema.png) calls an _action_).
		- The second converts that combined data into text protocol buffers in the draft data act schema. The mapping from the schema to the SBA data can be found in `mappings/sba.py`.
	
6. Validating the data
	- *Build "validation engine" that verifies mapping to DATA Act Schema and integrity of the data:* This component verifies data have accurately been mapped from agency source systems to the DATA Act Schema. It will apply basic validation rules to verify data are accurate and consistent with the DATA Act Schema metadata. 
	
	------
	*For the SBA pilot*
	- An initial stab at a validator can be found at [processors/validator.py](../processors/validator.py). Rules are added as simple python objects, but could be pulled out of the script and parsed at runtime.
	- Proposed rules are being documented at [sba-business-rules.md](../sba-business-rules.md).

7. Providing validation reports
8. Submitting data to Treasury 


###Agency support:

OMB and Treasury are committed to maintaining strong communication with agencies by: 

- Holding phone calls with Senior Accoutable Official
- Compiling a bi-weekly DATA Act Activities 
- Conducting agency implementation workshops
