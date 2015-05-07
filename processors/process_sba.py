import csv
import argparse 
from mappings.sba import schema_map
from schema.data_act_schema_pb2 import Action, AgencyTransaction, Amount, TreasuryAccountSymbol, Account, Agency, Award, PlaceOfPerformance, Awardee, Address, HighlyCompensatedOfficer

def open_input_file(filename):
    # open combined file
    f = csv.DictReader(open(filename))
    return f

def open_output_file(outfile=None):
    if not outfile:
        outfile = 'sbadata.txt'
    return open(outfile, 'w')

def process_record(record):
    
    schema_record = Action()
    schema_record.award = Award()
    schema_record.award.awardee = Awardee()
    schema_record.award.awardee.businessAddress = Address()

    for schema_field, sba_field in schema_map.items():
        try:
            if callable(sba_field):
                #it's a function not a fieldname
                value = sba_field(record)
            else:
                #assign value to correct attribute
                value = record[sba_field]
            
            #set value on record
        except KeyError:
            value = None

        if value:
            #eval('obj = schema_record.{0}'.format(schema_field))
            #obj = value
            schema_record.award.awardees[0].businessAddress.street1 = 'bla'
    return schema_record

def run():
    
    parser = argparse.ArgumentParser(description="Take in a file with SBA data and output a compiled protobuf file in the DATA act schema")
    parser.add_argument('-i', dest='infile', required=True, help='the infile that contains SBA data')
    parser.add_argument('-o', dest='outfile', help='the outfile that will contain the processed data')

    args = parser.parse_args()
    data = open_input_file(args.infile)
    output = open_output_file()

    for record in data: 
        #turn CSV row or whole csv into dict
        new_rec = process_record(record)
        output.write(new_rec.SerializeToString())

   # record validation errors
   # write out to file for uploading (compiled instances of protobuf messages)


run()   


