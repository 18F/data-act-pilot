---
title: DATA Act business rules
---
As an SBA user, I need to see the business rules being applied to my source data

Business rules or validation rules will be applied to ensure that submitted data by the US Small Business Administration meets the DATA Act criteria. Goals of these validation rules will improve cleanliness, accuracy, and meaningfulness of the data set. Below is a draft of proposed rules and are subject to change. 

*Standard validation*

Required fields: 
	Required field validation ensures that users input data in required fields. If field is empty, an error will raise. [data-act schema](https://github.com/18F/intercessor/blob/master/schema/data-act-schema.png)

Data types: 
	Data type validation ensures that the data types match with the [DATA Act schema](https://github.com/18F/intercessor/blob/master/schema/data-act-schema.png) . If parentAward data type required is a string, entering an number will raise an error. 


*Awardee validation:*  
	Award ID validation ensures that the Award ID is exact number length (if it is not blank). Also ensures DUNSNumber and SAM number match. 
	Address:
		Address validation ensures that users input data in the Awardee Address fields. If fields are empty, an error will raise. 
		state and zip codes: Validates that the vendor Zip/Postal Code is valid by looking up the first five characters of the value in the Address: postalCode that contains a record for every valid zip code in the US. If the zip code is not found in the Zip_Code__c object, or the Billing State does not match the corresponding State_Code__c in the Zip_Code__c object, an error is displayed. 
	
Award validation: 
	ObjectClass: NACIS Code 
	CFDA Code: 


Questions: 

- How do you keep track of changing addresses? 
- Is it more important that the validation be associated with the current address or does it need to be when the award was issued? 
- What are the authoritative sources to validate addresses, NACIS code, CFDA code? 



 
