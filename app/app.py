
import csv
import logging
import os
import sys
from functools import wraps

from flask import Flask, request, Response, url_for, render_template

app = Flask(__name__)
username = os.getenv('WEB_USERNAME', '')
password = os.getenv('WEB_PASSWORD', '')

ALLOWED_EXTENSIONS = ['csv']
VALIDATION = {
    'appropriation.csv': ['header1', 'header2'],
    'object_class_program_activity.csv': [],
    'award.csv': [],
    'award_financial.csv': []
}

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(ch)

def allowed_file(filename):
    """Checks if the filename is an allowed type of file.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def validate_headers(csv_file, correct_headers):
    reader = csv.reader(csv_file)
    row_count = sum(1 for row in reader)
    if row_count < 1:
        return False
    headers = next(reader)

    return not headers == correct_headers

def check_file(file, valid_headers, template_name):
    error = {}
    error['template_name'] = template_name
    if not file:
        error['message'] = 'File was not uploaded'
        return error
    error['filename'] = file.filename or ''
    if not allowed_file(file.filename):
        error['message'] = 'File is of incorrect type'
        return error
    if not validate_headers(file, valid_headers):
        error['message'] = 'File headers are incorrect'
        return error

    return None

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
        files = request.files
        log.warn('files')
        log.warn(files)
        file_errors  = []
        for name in VALIDATION.keys():
            error = check_file(files[name], VALIDATION[name], name)
            if error:
                file_errors.append(error)

        log.warn('errors')
        log.warn(file_errors)
        return render_template('home.html', file_errors=file_errors)

    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
