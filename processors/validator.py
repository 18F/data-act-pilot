import schema.data_act_schema_pb2
from google.protobuf import text_format
from protobuf_to_dict import protobuf_to_dict
import codecs
import argparse
import itertools

REQUIRED_FIELDS = [
    'award.awardingAgency.officeCode',
    'award.awardees.businessName',
    'award.awardees.businessAddress.street1',
    'award.awardees.businessAddress.city',
    'award.awardees.businessAddress.state',
    'award.awardees.businessAddress.postalCode'
    ]
LENGTHS = [
    ('award.awardingAgency.officeCode', 6),
    ('award.fundingAgency.officeCode', 6)]
NUMERIC_FIELDS = ['transaction.programActivity']
POSSIBLE_VALUES = [
    ('transaction.objectClass', ['4110', '4101']),
    ('award.awardees.businessType', ['0', '1','2','3','4','5', '6', '11','12','20','21','22','23','25'])
    ]


REPEATED_FIELDS = [
    'award.awardees',
    'award.placesOfPerformance',
    'award.awardees.highlyCompensatedOfficers',
    'transaction.outlays',
]


def get_values(field, record):
    result = []
    try:
        value = reduce(dict.__getitem__, field.split('.'), record)
        if isinstance(value, list):
            result = value
        else:
            result.append(value)
    except KeyError:
        result.append('')
    except TypeError:
        for repeated_field in REPEATED_FIELDS:
            if field.startswith(repeated_field) and repeated_field != field:
                records = get_values(repeated_field, record)
                for r in records:
                    new_field = field.replace(repeated_field + '.', '')
                    result.append(get_values(new_field, r))
    if all([isinstance(l, list) for l in result]):
        result = list(itertools.chain.from_iterable(result))
    return result


def check_required_fields(record):
    result = []
    for field in REQUIRED_FIELDS:
        for value in get_values(field, record):
            if not value:
                result.append("Required field {0} missing".format(field))
    return result


def check_lengths(record):
    result = []
    for field, length in LENGTHS:
        for value in get_values(field, record):
            if value:
                if len(value) != length:
                    result.append("Value of {0} must be exactly "
                                  "{1} characters".format(field, length))
    return result


def check_numeric_fields(record):
    result = []
    for field in NUMERIC_FIELDS:
        for value in get_values(field, record):
            if value:
                try:
                    float(value)
                except ValueError:
                    result.append("Value of {0} must be numeric".format(field))
    return result

def check_enums(record):
    result = []
    for field, enum in POSSIBLE_VALUES:
        for value in get_values(field, record):
            if value not in enum:
                result.append("Value of {0} must be one of {1}".format(field, enum))
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
    error_count = 0
    errors = {}
    for record in records:
        record_count += 1
        results = []
        results += check_required_fields(record)
        results += check_lengths(record)
        results += check_numeric_fields(record)
        results += check_enums(record)
        if results:
            error_count += len(results)
            errors[str(record_count)] = results
    print('Parsed {0} records and found {1} errors.'.format(record_count, error_count))
    print('\n')
    for rec, errs in errors.iteritems():
        if errs:
            print('In record {0}, the following errors were found:'.format(rec))
            for err in errs:
                print(err)
