import schema.data_act_schema_pb2
from google.protobuf import text_format
from protobuf_to_dict import protobuf_to_dict
import codecs
import argparse

REQUIRED_FIELDS = [
    'award.awardingAgency.officeCode',
    'award.actionDate'
    ]
LENGTHS = [('award.awardingAgency.officeCode', 6)]
NUMERIC_FIELDS = ['transaction.programActivity']
POSSIBLE_VALUES = [
    ('transaction.objectClass', ['4110', '4101']),
    ('award.awardees.businessType', ['0', '1','2','3','4','5', '6', '11','12','20','21','22','23','25',])
    ]


def get_dot_notation(field, record):
    try:
        result = reduce(dict.__getitem__, field.split('.'), record)
    except KeyError:
        result = []
    return result


def check_required_fields(record):
    result = []
    for field in REQUIRED_FIELDS:
        if not get_dot_notation(field, record):
            result.append("Required field {0} missing".format(field))
    return result


def check_lengths(record):
    result = []
    for field, length in LENGTHS:
        value = get_dot_notation(field, record)
        if value:
            if len(value) != length:
                result.append("Value of {0} must be exactly "
                              "{1} characters".format(field, length))
    return result


def check_numeric_fields(record):
    result = []
    for field in NUMERIC_FIELDS:
        value = get_dot_notation(field, record)
        if value:
            try:
                float(value)
            except ValueError:
                result.append("Value of {0} must be numeric".format(field))
    return result


def check_enums(record):
    result = []
    for field, values in POSSIBLE_VALUES:
        value = get_dot_notation(field, record)
        if value:
            if value not in values:
                result.append("{0} must be one of: {1}".format(field, values))
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(
        'Schema Act Data Validation. Takes text format protobuf messages '
        'and applies validation rules.'))
    parser.add_argument('-i', dest='infile',
                        help=('A file of double newline delimited text format '
                              'protobufs.'))
    args = parser.parse_args()
    infile = args.infile
    with codecs.open(infile, 'r', 'utf-8') as f:
        pbs = f.read()
    pbs = pbs.split('\n\n')
    records = []
    for pb in pbs:
        record = schema.data_act_schema_pb2.Action()
        text_format.Merge(pb, record)
        record = protobuf_to_dict(record)
        records.append(record)
    record_count = 0
    for record in records:
        record_count += 1
        results = []
        results += check_required_fields(record)
        results += check_lengths(record)
        results += check_numeric_fields(record)
        results += check_enums(record)
        if results:
            print('\n')
            print('In record {0}, the following errors were found:'.format(record_count))
            for result in results:
                print(result)
