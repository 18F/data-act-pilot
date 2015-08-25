
import csv
import logging
import os
import re
import sys
from functools import wraps

from flask import Flask, request, Response, url_for, render_template
from flask.ext.babel import Babel

from validator.validator import ValidatorSingle


app = Flask(__name__)
username = os.getenv('WEB_USERNAME', '')
password = os.getenv('WEB_PASSWORD', '')
app.jinja_env.add_extension('jinja2.ext.i18n')
babel = Babel(app)

RULES_DIR = './rules/'

ALLOWED_EXTENSIONS = ['csv']
# TODO create this dict dynamically by reading csv schema files.
VALIDATION = {
    'appropriation.csv': [
        'AllocationTransferAgencyIdentifier',
        'AgencyIdentifier',
        'BeginningPeriodOfAvailability',
        'EndingPeriodOfAvailability',
        'AvailabilityTypeCode',
        'MainAccountCode',
        'BudgetAuthorityAppropriatedAmount',
        'UnobligatedAmount',
        'OtherBudgetaryResourcesAmount'
        ],
    'object_class_program_activity.csv': [
        'AllocationTransferAgencyIdentifier',
        'AgencyIdentifier',
        'BeginningPeriodOfAvailability',
        'EndingPeriodOfAvailability',
        'AvailabilityTypeCode',
        'MainAccountCode',
        'ObjectClass',
        'ObligatedAmount',
        'ProgramActivity',
        'OutlayAmount'
        ],
    'award.csv': [
        'piidPrefix',
        'piidAwardYear',
        'piidAwardType',
        'piidAwardNumber',
        'FainAwardNumber',
        'AwardDescription',
        'AwardModAmendmentNumber',
        'ParentAwardIDprefix',
        'ParentAwardYear',
        'ParentAwardType',
        'ParentAwardNumber',
        'RecordType',
        'ActionDateDay',
        'ActionDateMonth',
        'ActionDateYear',
        'TypeOfAction',
        'ReasonForModification',
        'TypeOfContractPricing',
        'idvType',
        'ContractAwardType',
        'AssistanceType',
        'FederalPrimeAward',
        'NonFederalFundingAmount',
        'CurrentTotalFundingObligationAmount',
        'CurrentTotalValueAwardAmount',
        'FaceValueLoanGuarantee',
        'PotentialTotalValueAwardAmount',
        'AwardingAgencyName',
        'AwardingAgencyCode',
        'AwardingSubTierAgencyName',
        'AwardingSubTierAgencyCode',
        'AwardingOfficeName',
        'AwardingOfficeCode',
        'FundingAgencyName',
        'FundingAgencyCode',
        'FundingSubTierAgencyName',
        'FundingOfficeName',
        'FundingOfficeCode',
        'RecipientLegalEntityName',
        'RecipientDunsNumber',
        'RecipientUltimateParentUniqueId',
        'RecipientUltimateParentLegalEntityName',
        'RecipientLegalEntityAddressStreet1',
        'RecipientLegalEntityAddressStreet2',
        'RecipientLegalEntitylCityName',
        'RecipientLegalEntityStateCode',
        'RecipientLegalEntityZip',
        'RecipientLegalEntityZip+4',
        'RecipientLegalEntityPostalCode',
        'RecipientLegalEntityCongresionalDistrict',
        'RecipientLegalEntityCountryCode',
        'RecipientLegalEntityCountryName',
        'HighCompOfficer1FirstName',
        'HighCompOfficer1MiddleInitial',
        'HighCompOfficer1LastName',
        'HighCompOfficer2FirstName',
        'HighCompOfficer2MiddleInitial',
        'HighCompOfficer2LastName',
        'HighCompOfficer3FirstName',
        'HighCompOfficer3MiddleInitial',
        'HighCompOfficer3LastName',
        'HighCompOfficer4FirstName',
        'HighCompOfficer4MiddleInitial',
        'HighCompOfficer4LastName',
        'HighCompOfficer5FirstName',
        'HighCompOfficer5MiddleInitial',
        'HighCompOfficer5LastName',
        'HighCompOfficer1Amount',
        'HighCompOfficer2Amount',
        'HighCompOfficer3Amount',
        'HighCompOfficer4Amount',
        'HighCompOfficer5Amount',
        'BusinessType',
        'NAICS_Code',
        'NAICS_Description',
        'CFDA_Code',
        'CFDA_Description',
        'PeriodOfPerfStartDay',
        'PeriodOfPerfStartMonth',
        'PeriodOfPerfStartYear',
        'PeriodOfPerfCurrentEndDay',
        'PerioOfPerfCurrentEndMonth',
        'PeriodOfPerfCurrentEndYear',
        'PeriodOfPerfPotentialEndDay',
        'PeriodOfPerfPotentialEndMonth',
        'PeriodOfPerfPotentialEndYear',
        'OrderingPeriodEndDay',
        'OrderingPeriodEndMonth',
        'OrderingPeriodEndYear',
        'PlaceOfPerfCity',
        'PlaceOfPerfState',
        'PlaceOfPerfCounty',
        'PlaceOfPerfZip+4',
        'PlaceOfPerfCongressionalDistrict',
        'PlaceOfPerfCountryName'
        ],
    'award_financial.csv': [
        'AllocationTransferAgencyIdentifier',
        'AgencyIdentifier',
        'BeginningPeriodOfAvailability',
        'EndingPeriodOfAvailability',
        'AvailabilityTypeCode',
        'MainAccountCode',
        'ParentAwardIDprefix',
        'ParentAwardYear',
        'ParentAwardType',
        'ParentAwardNumber',
        'FainAwardNumber',
        'AwardModAmendmentNumber',
        'ObjectClass',
        'TransactionObligatedAmount'
        ]
}

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(ch)

@app.template_filter('regex_replace')
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)


def file_info(file_obj, template_name, errors, err_message=''):
    return {
        'filename': file_obj.filename or '',
        'template_name': template_name[:-4].replace('_', ' ').capitalize(),
        'message': err_message,
        'errors': errors
    }

def allowed_file(filename):
    """Checks if the filename is an allowed type of file.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def validate_headers(csv_file, correct_headers):
    reader = csv.reader(csv_file)
    try:
        headers = reader.next()
    except StopIteration:
        return False

    csv_file.seek(0)
    return sorted(headers) == sorted(correct_headers)

def check_file(file, valid_headers, template_name):
    message = ''
    if not file:
        message = 'File was not uploaded'
        return file_info(file, template_name, [], message)
    if not allowed_file(file.filename):
        message = 'File is of incorrect type'
        return file_info(file, template_name, [], message)
    if not validate_headers(file, valid_headers):
        message = 'File headers are incorrect'
        return file_info(file, template_name, [], message)

    return None

def validate_file(file, template_name):
    validator = ValidatorSingle(
            file,
            template_name,
            RULES_DIR)

    return validator.results

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
        log.warning('post')
        correct_files = []
        files = request.files
        wrong_files  = []
        invalid_files = []
        for name in VALIDATION.keys():
            error = check_file(files[name], VALIDATION[name], name)
            if error:
                wrong_files.append(error)
            else:
                error = validate_file(files[name], name)
                if error:
                    invalid_files.append(file_info(
                       files[name],
                       name,
                       error
                        ))
                else:
                    correct_file.append(file_info(
                        files[name],
                        name,
                        []
                        ))

        return render_template('home.html',
                                correct_files=correct_files,
                                invalid_files=invalid_files,
                                wrong_files=wrong_files)

    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
