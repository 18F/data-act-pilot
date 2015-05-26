import argparse
import os
import requests
from pprint import pprint

fields = ['duns', 'duns4', 'cage', 'ncage', 'dodaac', 'purposeOfRegistration',
          'registrationDate', 'expirationDate', 'activationDate',
          'lastUpdatedDate', 'legalBusinessName', 'doingBusinessAsName',
          'companyDivision', 'divisionNumber', 'samAddress',
          'congressionalDistrict', 'businessStartDate', 'fiscalYearCloseDay',
          'corporateUrl', 'corporateStructureCode',
          'corporateStructureDescription', 'mailingAddress',
          'stateOfIncorporation', 'countryOfIncorporation', 'govtBusinessPoc',
          'altGovtBusinessPoc', 'pastPerformancePoc', 'altPastPerformancePoc',
          'electronicBusinessPoc', 'altElectronicBusinessPoc',
          'creditCardUsage', 'hasDelinquentFederalDebt', 'hasKnownExclusion',
          'correspondenceFlag', 'status', 'statusMessage', 'businessTypes',
          'sbaCertificationExpirationDate', 'disasterRelief', 'pscCodes',
          'certifications', 'qualifications']


class SamData(object):
    def __init__(self, duns):
        if len(duns) == 9:
            self.duns = duns + '0000'
        elif len(duns) == 13:
            self.duns = duns
        else:
            raise ValueError('Invalid DUNS number.')
        self.sam_data = self.get_sam_data(duns)
        self.sample_duns = '1132780760000'

    def get_sam_data(self, duns):
        base_url = 'https://api.data.gov/sam/v1/registrations/'
        api_key = os.environ['DOT_GOV_API_KEY']
        req = requests.get(base_url + str(duns) + '?api_key=' + api_key)
        sam_data = {}
        results = req.json()
        if 'sam_data' in results:
            if 'registration' in results['sam_data']:
                sam_data = results['sam_data']['registration']
        return sam_data

    def get_field(self, fieldname, sam_data):
        return sam_data.get(fieldname)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description=(
        'Takes a DUNS number and prints the SAM api json response to stdout. '
        'Optionally provide a list of requested fields.'))
    parser.add_argument('duns', help="DUNS or DUNS+4")
    parser.add_argument('-f', '--fields', nargs='*', help="A list of fields.",
                        choices=fields)

    args = parser.parse_args()
    data = SamData(args.duns)
    if args.fields:
        results = {k: data.get_field(k, data.sam_data) for k in args.fields}
        if 'duns' not in results:
            results['duns'] = data.get_field('duns', data.sam_data)
    else:
        results = data.sam_data
    pprint(results)
