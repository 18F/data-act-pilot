# Converting to XBRL (Draft schema v0.5)

From the command line, run:

` $ python xbrl_translate <path-to-appropriation-csv> <path-to-object-class-csv> <path-to-award-financial-csv> <path-to-award-csv> output-dir `

Note that all files must be present for the translator to run. Currently, due to missing data and a desire to get something up and running, the translator will stick default values into the xml when fields are missing.

The output is a single file containing financial level data, and one file per award containing the award level data.