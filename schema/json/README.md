# About This Schema

For the purposes of exploration, this is a JSON schema representation of CSV formats used by the DATA Act pilot for ingestion of data from agencies. This example uses the [Tabular Data Package](http://dataprotocols.org/tabular-data-package/) format for representing a complete set of related data tables using common open-source formats:

* Each table of data is represented with a CSV
* An accompanying `datapackage.json` file provides information about the tables' schemas as well as information about the package as a whole.

Each CSV's individual schemas are represented within the `datapackage.json` with records described in the [JSON Table Schema](http://dataprotocols.org/json-table-schema/) format. For convenience, I have also provided these as four separate files for validation scripts that only understand the JSON Table Schema format. These are extracted directly from the datapackage.json file.