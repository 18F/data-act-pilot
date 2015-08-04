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

    def load_data(self, filepath):
        '''Loads data from submitted agency CSV

        Expects:
            filepath: path to the CSV to be loaded
        Outputs:
            A list of dicts produced by csv.DictReader'''

        return [row for row in csv.DictReader(open(filepath))]

    def load_simple_rules(self, rules_file):
        rules_dict = {}
        rules = csv.DictReader(open(rules_file, 'rU'))
        for row in rules:
            rules_dict[row['fieldname']] = row
        return rules_dict

    def check_required(self, required, value):
        if not eval(required) or value:
                return True

    def check_data_type(self, data_type, value):
        if type(value) == eval(data_type):
            return True

    def check_length(self, length, value):
        if len(value) <= length:
            return True

    def check_unique(self, value):
        ''' TODO: micahsaul'''
        pass

    def generate_error(self,
                       error_type,
                       fieldname,
                       hard_fail=True,
                       data_type='',
                       length=''):
        result = {}
        result['error_type'] = error_type
        result['hard_fail'] = hard_fail
        result['fieldname'] = fieldname
        result['error_string'] = eval(ERROR_STRINGS[error_type])
        return result

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
                    error = self.generate_error('required_error', field)
                    results.append(error)
                if not self.check_data_type(rule['data_type'], row[field]):
                    error = self.generate_error('type_error',
                                                field,
                                                data_type=rule['data_type'])
                    results.append(error)
                if not self.check_length(rule['field_length'], row[field]):
                    error = self.generate_error('len_error',
                                                field,
                                                length=rule['field_length'])
                    results.append(error)
            else:
                raise TypeError('Field {} not recognized.'.format(field))
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
                          args.rules_dir)
    pprint(validator.results)
