
import csv
import logging
import os
import re
import sys
import tempfile
from functools import wraps
import pandas as pd
import time
import glob
import re

from flask import Flask, request, Response, url_for, render_template
from flask.ext.babel import Babel

from validator.validator import ValidatorSingle


app = Flask(__name__)
username = os.getenv('WEB_USERNAME', '')
password = os.getenv('WEB_PASSWORD', '')
app.jinja_env.add_extension('jinja2.ext.i18n')
babel = Babel(app)

RULES_DIR = './rules/'
RULES_FILES = glob.glob(os.path.join(os.path.dirname(__file__),
                                     'validator/rules/*.csv'))

ALLOWED_EXTENSIONS = ['csv']

VALIDATION = {}
for rule_file in RULES_FILES:
    file_df = pd.read_csv(rule_file)
    file_name = re.sub('_rules', '', rule_file.split('/')[-1])
    field_list = file_df['fieldname'].tolist()
    VALIDATION[file_name] = field_list

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(ch)

@app.template_filter('regex_replace')
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)


def file_info(file_obj, template_name, errors, err_message='', err_detail='', csv_location=''):
    return {
        'filename': file_obj.filename or '',
        'template_name': template_name[:-4].replace('_', ' ').capitalize().strip(),
        'message': err_message,
        'detail': err_detail,
        'errors': errors,
        'csv_location': csv_location
    }

def allowed_file(filename):
    """Checks if the filename is an allowed type of file.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def validate_headers(dataframe, correct_headers):
    try:
        headers = list(dataframe.columns.values)
    except:
        return (False)

    #ignore extra columns in the uploaded files
    #return set(correct_headers).issubset(set(headers))
    valid = set(correct_headers).issubset(set(headers))
    extra = [h for h in correct_headers if h not in headers]
    return (valid, extra)

def check_file(file, dataframe, valid_headers, template_name):
    message = ''
    detail = ''
    if not file:
        message = 'File was not uploaded'
        detail = 'Use the form to upload all four of the files'
        return file_info(file, template_name, [], message, err_detail=detail)
    if not allowed_file(file.filename):
        message = 'File is of incorrect type'
        detail = 'The uploaded file must be a .csv file'
        return file_info(file, template_name, [], message, err_detail=detail)
    headers = validate_headers(dataframe, valid_headers)
    if not headers[0]:
        message = 'File headers don\'t match the DATA Act \
            template'
        detail = 'The following fields were not found in the header row of your file: '
        detail += ', '.join(headers[1])
        return file_info(file, template_name, [], message, err_detail=detail)

    return None

def validate_file(dataframe, template_name):
    validator = ValidatorSingle(
            dataframe,
            template_name,
            RULES_DIR)
    if len(validator.results[0]):
        return validator.results
    else:
        return None

def strip_value(value):
    """Strip whitespace from beginning and end of incoming data
    """
    if type(value) == str:
        return value.strip()
    else:
        return value

def check_auth(ausername, apassword):
    """Checks that the username / password combination is valid for basic
    HTTP auth.
    """
    return ausername == username and apassword == password

def authenticate():
    return Response(
        'Could not verify your access level for this url.\n'
        'Please login with username and password', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET', 'POST'])
@requires_auth
def hello_world():
    if request.method == 'POST':
        correct_files = []
        files = request.files
        dataframes = {}
        invalid_files = []
        for name in VALIDATION.keys():
            try:
                dataframe = pd.read_csv(files[name].stream)
                dataframe = dataframe.fillna('')
                dataframe = dataframe.applymap(strip_value)
                files[name].seek(0)
            except:
                dataframe = pd.DataFrame()
            error = check_file(files[name], dataframe, VALIDATION[name], name)
            if error:
                invalid_files.append(error)
            else:
                error = validate_file(dataframe, name)
                if error:
                    filename = (name[:-4] +
                                str(time.time()).replace('.', '') +
                                '.csv')
                    filepath = os.path.join(os.path.dirname(__file__),
                                            'static',
                                            'csvs',
                                            filename)
                    with open(filepath, 'w') as f:
                        writer = csv.writer(f,
                                            delimiter=',',
                                            quotechar='"',
                                            quoting=csv.QUOTE_MINIMAL)
                        headers = ['Error Row Number']
                        errs = error[0]
                        k = errs[errs.keys()[0]]
                        if k.get('tas_identifier'):
                            headers.append('TAS')
                        for identifier in k['identifiers']:
                            headers.append(identifier)
                        headers += ['Fieldname', 'Value', 'Error']
                        writer.writerow(headers)
                        for key, row in errs.iteritems():
                            for err in row['errors']:
                                output = []
                                output.append(key.split('_')[-1][3:])
                                if row.get('tas_identifier'):
                                    output.append(row['tas_identifier'])
                                for value in row['identifiers'].values():
                                    output.append(value)
                                output.append(err['fieldname'])
                                output.append(err['value'])
                                output.append(err['error_string'])
                                writer.writerow(output)
                    invalid_files.append(file_info(
                                         files[name],
                                         name,
                                         error,
                                         err_message='Some fields are invalid',
                                         err_detail=('Check the specific '
                                                     'errors below and edit '
                                                     'the source data'),
                                         csv_location=filename))
                else:
                    correct_files.append(file_info(
                        files[name],
                        name,
                        []
                        ))

        return render_template('home.html',
                               correct_files=correct_files,
                               invalid_files=invalid_files)

    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
