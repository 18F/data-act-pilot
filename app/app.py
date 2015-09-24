
import csv
import logging
import os
import re
import sys
from functools import wraps
import pandas as pd

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
        'FundingSubTierAgencyCode',
        'FundingOfficeName',
        'FundingOfficeCode',
        'RecipientLegalEntityName',
        'RecipientDunsNumber',
        'RecipientUltimateParentUniqueId',
        'RecipientUltimateParentLegalEntityName',
        'RecipientLegalEntityAddressStreet1',
        'RecipientLegalEntityAddressStreet2',
        'RecipientLegalEntityCityName',
        'RecipientLegalEntityStateCode',
        'RecipientLegalEntityZip',
        'RecipientLegalEntityZip+4',
        'RecipientLegalEntityPostalCode',
        'RecipientLegalEntityCongressionalDistrict',
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


def file_info(file_obj, template_name, errors, err_message='', err_detail=''):
    return {
        'filename': file_obj.filename or '',
        'template_name': template_name[:-4].replace('_', ' ').capitalize().strip(),
        'message': err_message,
        'detail': err_detail,
        'errors': errors
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
        return False

    return sorted(headers) == sorted(correct_headers)

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
    if not validate_headers(dataframe, valid_headers):
        message = 'File spreadsheet headers don\'t match with the data act \
            template'
        detail = 'Ensure csv file has the same headers as the templates'
        return file_info(file, template_name, [], message, err_detail=detail)

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
        correct_files = []
        files = request.files
        dataframes = {}
        invalid_files = []
        for name in VALIDATION.keys():
            try:
                dataframe = pd.read_csv(files[name].stream)
                files[name].seek(0)
            except:
                dataframe = pd.DataFrame()
            error = check_file(files[name], dataframe, VALIDATION[name], name)
            if error:
                invalid_files.append(error)
            else:
                error = validate_file(files[name], name)
                if error:
                    invalid_files.append(file_info(
                       files[name],
                       name,
                       error,
                       err_message='Some fields are not valid',
                       err_detail='Check the specific errors below and edit the \
                           source data'
                        ))
                else:
                    correct_file.append(file_info(
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
