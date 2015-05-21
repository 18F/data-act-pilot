---
title: DATA Act business rules
---
As an SBA user, I need to see the business rules being applied to my source data

Business rules or validation rules will be applied to ensure that submitted data by the US Small Business Administration meets the DATA Act criteria. Goals of these validation rules will improve cleanliness, accuracy, and meaningfulness of the data set. Below is a draft of proposed rules and are subject to change. 

*Standard validation*

Required fields: 
	Required field validation ensures that users input data in required fields. If field is empty, an error will be raised. Required fields to be determined in the [DATA act schema](https://github.com/18F/intercessor/blob/master/schema/data-act-schema.png)

Data types: 
	Data type validation ensures that the data types match with the [DATA Act schema](https://github.com/18F/intercessor/blob/master/schema/data-act-schema.png) . For example, `parentAward` data type required is a string, If a number is entered an error will be raised. 


*Awardee validation:*  
	Award id validation ensures that `Award id` is an exact number length (if it is not blank). This length can be determined and set. Additionally, award id validation ensures DUNSNumber and SAM number match. If either of those criterias are not met an error will be raised
	Address:
		Address validation ensures that users input data in the Awardee Address fields. If fields are empty, an error will be raised. 
		state and zip codes validation will ensure that Awardee Zip/Postal Code is valid by looking up the first five characters of the value in a zip code object that contains a record for every valid zip code in the US. If the zip code is not found in the zip code object, an error will be raised. 
	
Award validation: 
	ObjectClass: NACIS Code 
	CFDA Code: 


Questions: 

- How do you keep track of changing addresses? 
- Is it more important that the validation be associated with the current address or does it need to be when the award was issued? 
- Will you have a list of valid state codes and zip codes? 
- What are the authoritative sources to validate addresses, NACIS code, CFDA code? 



 
