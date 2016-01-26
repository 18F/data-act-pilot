import argparse
import csv
import os
from pprint import pprint


ERROR_STRINGS = {
    'uniqueness_error': '"{0} must be unique.".format(fieldname)',
    'required_error': '"Required field {0} is missing.".format(fieldname)',
    'type_error': '"{0} must be of type {1}.".format(fieldname, data_type)',
    'len_error': ('"{0} must be no more than {1} characters.".format'
                  '(fieldname, length)')
}
TAS_KEY_IDENTIFIERS = [
    'AllocationTransferRecipientAgencyId',
    'AgencyIdentifier',
    'BeginningPeriodOfAvailability',
    'EndingPeriodOfAvailability',
    'AvailabilityTypeCode',
    'MainAccountCode'
]
KEY_IDENTIFIERS = {
    'appropriation': [],
    'object_class_program_activity': [
        'ProgramActivityCode',
        'ObjectClass'
    ],
    'award': [
        'FainAwardNumber'
    ],
    'award_financial': [
        'ObjectClass',
        'FainAwardNumber'
    ]
}


class Validator(object):
    '''A validator which will read in 4 csv files and
    perform various validations'''

    def __init__(self,
                 appropriation_file,
                 object_class_file,
                 award_financial_file,
                 award_file,
                 rules_dir):
        self.appropriations = self.load_data(appropriation_file)
        self.object_class = self.load_data(object_class_file)
        self.award_financial = self.load_data(award_financial_file)
        self.award = self.load_data(award_file)
        self.appropriations_rules = self.load_simple_rules(rules_dir +
                                                      'appropriation_rules.csv')
        self.object_class_rules = self.load_simple_rules(rules_dir +
                                                    'object_class_program_activity_rules.csv')
        self.award_financial_rules = self.load_simple_rules(rules_dir +
                                                       'award_financial_rules.csv')
        self.award_rules = self.load_simple_rules(rules_dir + 'award_rules.csv')

        self.results = self.validate_submission()

    def load_data(self, dataframe):
        '''Loads data from submitted agency CSV

        Expects:
            dataframe: dataframe of the agency-submitted CSV
        Outputs:
            A list of dicts'''

        if dataframe is None:
            return ''
        return dataframe.to_dict('records')

    def load_simple_rules(self, rules_file):
        base = os.path.dirname(__file__)
        filepath = filename = os.path.join(base, rules_file)
        rules_dict = {}
        rules = csv.DictReader(open(filepath, 'rU'))
        for row in rules:
            rules_dict[row['fieldname']] = row
        return rules_dict

    def check_required(self, required, value):
        if not eval(required) or value:
                return True
        elif value == 0:
            return True

    def check_data_type(self, data_type, value):
        try:
            eval(data_type)(value)
            return True
        except ValueError:
            return False

    def check_length(self, length, value):
        if len(str(value)) <= int(length):
            return True

    def check_unique(self, value):
        ''' TODO: micahsaul'''
        pass

    def generate_error(self,
                       error_type,
                       fieldname,
                       submitted_value,
                       hard_fail=True,
                       data_type='',
                       length=''):
        result = {}
        result['error_type'] = error_type
        result['hard_fail'] = hard_fail
        result['fieldname'] = fieldname
        result['value'] = submitted_value
        result['error_string'] = eval(ERROR_STRINGS[error_type])
        return result

    def build_tas(self, data):
        #key = ''
        #for field in TAS_KEY_IDENTIFIERS:
         #   if data[field]:
          #      key += str(data[field]) + '-'

        #return key[:-1]
        return "" # just return blank string since TAS fields changed

    def build_key(self, data, fields):
        keys = {}
        for field in fields:
            is_key = data.get(field,None)
            if is_key:
                keys[field] = data[field]

        return keys

    def validate_row(self, row, rules):
        '''Runs a set of simple validation rules against submitted data.

        Expects:
            data: A single dict from the list produced by load_data()
            rules: A dict of simple validation rules from load_simple_rules
        Outputs:
            A list of validation errors and metadata'''

        results = []
        for field in row:
            if field in rules:
                rule = rules[field]
                if not self.check_required(rule['required'], row[field]):
                    error = self.generate_error('required_error', field, 'n/a')
                    results.append(error)
                    continue
                if row[field]:
                    if not self.check_data_type(rule['data_type'], row[field]):
                        error = self.generate_error('type_error',
                                                    field,
                                                    row[field],
                                                    data_type=rule['data_type'])
                        results.append(error)
                    if not self.check_length(rule['field_length'], row[field]):
                        error = self.generate_error('len_error',
                                                    field,
                                                    row[field],
                                                    length=rule['field_length'])
                        results.append(error)
            else:
                #for the prototype, ignore extra columns on submitted csvs
                pass
        return results

    def validate_file(self, filename, data, rules):
        '''Runs all validations on a single file.

        Expects:
            filename: The type of file being validated.
            data: A list of dicts produced by load_data()
            rules: A dict of simple validation rules from load_simple_rules()
        Outputs:
            A dict, keyed by a docname + row number, containing errors and
            original data.
        '''
        results = {}
        row_count = 0
        for row in data:
            row_count += 1
            errors = self.validate_row(row, rules)
            if errors:
                row_id = filename + '_row' + str(row_count)
                result = {}
                result['errors'] = errors
                result['data'] = row
                if filename != 'award':
                    result['tas_identifier'] = self.build_tas(row)
                result['identifiers'] = self.build_key(
                        row, KEY_IDENTIFIERS[filename])
                results[row_id] = result
        return results

    def validate_submission(self):
        results = []
        results.append(self.validate_file('appropriations',
                                          self.appropriations,
                                          self.appropriations_rules))
        results.append(self.validate_file('object_class',
                                          self.object_class,
                                          self.object_class_rules))
        results.append(self.validate_file('award_financial',
                                          self.award_financial,
                                          self.award_financial_rules))
        results.append(self.validate_file('award',
                                          self.award,
                                          self.award_rules))
        return results

class ValidatorSingle(Validator):
    def __init__(self,
               file_dataframe,
               file_template,
               rules_dir):
        self.file_data = self.load_data(file_dataframe)
        self.file_template = file_template
        self.rules = self.load_simple_rules(rules_dir +
                file_template[:-4] + '_rules' + file_template[-4:])
        self.results = []
        self.results.append(self.validate_file(file_template[:-4],
                                               self.file_data,
                                               self.rules))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(
        'Validates the four CSV files in the DATA Act Agency submission'))
    parser.add_argument('appropriation', help="Appropriation CSV")
    parser.add_argument('object_class', help="Object Class CSV")
    parser.add_argument('award_financial', help="Award Financial CSV")
    parser.add_argument('award', help="Award CSV")
    parser.add_argument('rules_dir', help="Path to rules directory")

    args = parser.parse_args()

    validator = Validator(args.appropriation,
                          args.object_class,
                          args.award_financial,
                          args.award,
                          args.rules_dir
                          )
    pprint(validator.results)
