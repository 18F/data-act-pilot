# DATA Act Pilot Validations

The DATA Act broker pilot performs a two-step validation process on incoming data:

1. Makes sure the file is a .csv with the correct column names and number of columns. See the [how to guide](HOWTO.md "DATA Act Pilot How To") for more information about preparing your data.
2. Checks the file against a list of validation rules (sometimes called _business rules_). A list of these rules is below.

## Validation Rules

The goal of the pilot's validation rules is to ensure data cleanliness, accuracy, and meaningfulness. This early iteration of the broker prototype validates incoming data and displays any problems it finds (see the [how to guide](HOWTO.md "DATA Act Pilot How To") for more information).

This website does not save a report about your data or send any information to Treasury. Future versions may have an option to submit data to Treasury, but the files will have to pass validations first.

Below are the validations currently in place, derived from Treasury's Data Element guidance.

### Basic Validation Rules

* All required data elements on the file are present.
* All data types match those in the schema.
* All data elements have the expected length.
* The _cardinality_ of each data element is correct. In other words, data elements that are supposed to be unique within a specific file are not repeated.

[This folder](https://github.com/18F/data-act-pilot/tree/master/app/validator/rules "basic validation rules") contains the specific basic validation rules for all data elements in each of the four input files.

### Complex Validation Rules

The current version of the broker prototype does not perform the complex data rules defined in Treasury's Data Element Guidance.
