import argparse
from bs4 import UnicodeDammit
import codecs
import csv
import os
from unidecode import unidecode

import award as award_schema
import finassist
import gen
import ussgl
import xbrli


def fix_encoding(text):
    """ Some files contain unknown decoding. This cleans that up."""
    return unidecode(UnicodeDammit(text).unicode_markup)


def write_int(value=''):
    '''Helper function to write an XBRL integer'''
    if not value:
        value = 42424242424242424242424242
    return xbrli.integerItemType(value, unitRef='ID1', contextRef='ID2')


def write_string(value=''):
    '''Helper function to write an XBRL string'''
    if not value:
        value = ' '
    return xbrli.stringItemType(fix_encoding(value), contextRef='ID2')


def write_amount(value=''):
    '''Helper function to write an XBRL amount'''
    if not value:
        value = '42424242'
    return gen.amountItemType(value, unitRef='ID1', contextRef='ID2')


def get_or_undefined(d, k):
    '''Helper function for setting undefined enum values'''
    result = 'undefined'
    try:
        if d[k]:
            result = d[k]
    except:
        pass
    return result


def create_agency(identifier, name, office_name, office_id):
    '''Creates an agency as defined in the gen XBRL schema'''
    agency = gen.agency()
    office = gen.agencyOffice()
    office.officeIdentifier = write_int(office_id)
    office.officeName = write_string(office_name)
    agency.agencyIdentifier = write_int(identifier)
    agency.agencyName = write_string(name)
    agency.agencyOffice.append(office)
    return agency


def create_date(year, month, date):
    '''Helper function to create XBRL dates'''
    if not year:
        year = '1981'
    if not month:
        month = '10'
    if not date:
        date = '03'
    if len(month) == 1:
        month = '0' + month
    if len(date) == 1:
        date = '0' + date
    return xbrli.dateItemType('-'.join([year, month, date]), contextRef='ID1')


def create_tas_element(data):
    '''Creates a TAS element as defined in the gen XBRL schema'''
    tas = gen.treasuryAccountSymbol()
    tas.agency = create_agency(data.get('AgencyIdentifier'), '', '', '')
    tas.allocationTransferAgencyIdentifier.append(write_int(data.get('AllocationTransferAgencyIdentifier')))
    tas.mainAccountNumber = write_int(data.get('MainAccountCode'))
    tas.beginningPeriodOfAvailability.append(write_string(data.get('BeginningPeriodOfAvailability')))
    tas.endingPeriodOfAvailability.append(write_string(data.get('EndingPeriodOfAvailability')))
    tas.availabilityTypeCode = gen.availableTypeCodeItemType(data.get('AvailabilityTypeCode'), contextRef='ID2')
    return tas


def create_tas(data):
    '''Create TAS, with X for unknown elements'''
    tas = ''
    elements = ['AgencyIdentifier',
                'AllocationTransferAgencyIdentifier',
                'MainAccountCode',
                'SubAccountSymbol',
                'BeginningPeriodOfAvailability',
                'EndingPeriodOfAvailability',
                'AvailabilityTypeCode']
    for element in elements:
        if data.get(element):
            tas += data.get(element) + '-'
        else:
            tas += 'X-'
    return tas[:-1]


def index_by_tas(data):
    '''Helper function to create a dict from a list of dicts, indexed by tas'''
    indexed = {}
    for d in data:
        key = create_tas(d)
        if key in indexed:
            indexed[key].append(d)
        else:
            indexed[key] = [d]
    return indexed


def fix_state(state):
    '''Helper function to fix state codes'''
    state_codes = {'alabama': 'AL',
                   'alaska': 'AK',
                   'arizona': 'AZ',
                   'arkansas': 'AR',
                   'california': 'CA',
                   'colorado': 'CO',
                   'connecticut': 'CT',
                   'delaware': 'DE',
                   'florida': 'FL',
                   'georgia': 'GA',
                   'hawaii': 'HI',
                   'idaho': 'ID',
                   'illinois': 'IL',
                   'indiana': 'IN',
                   'iowa': 'IA',
                   'kansas': 'KS',
                   'kentucky': 'KY',
                   'louisiana': 'LA',
                   'maine': 'ME',
                   'maryland': 'MD',
                   'massachusetts': 'MA',
                   'michigan': 'MI',
                   'minnesota': 'MN',
                   'mississippi': 'MS',
                   'missouri': 'MO',
                   'montana': 'MT',
                   'nebraska': 'NE',
                   'nevada': 'NV',
                   'new hampshire': 'NH',
                   'new jersey': 'NJ',
                   'new mexico': 'NM',
                   'new york': 'NY',
                   'north carolina': 'NC',
                   'north dakota': 'ND',
                   'ohio': 'OH',
                   'oklahoma': 'OK',
                   'oregon': 'OR',
                   'pennsylvania': 'PA',
                   'rhode island': 'RI',
                   'south carolina': 'SC',
                   'south dakota': 'SD',
                   'tennessee': 'TN',
                   'texas': 'TX',
                   'utah': 'UT',
                   'vermont': 'VT',
                   'virginia': 'VA',
                   'washington': 'WA',
                   'west virginia': 'WV',
                   'wisconsin': 'WI',
                   'wyoming': 'WY',
                   'american samoa': 'AS',
                   'district of columbia': 'DC',
                   'federated states of micronesia': 'FM',
                   'guam': 'GU',
                   'marshall islands': 'MH',
                   'northern mariana islands': 'MP',
                   'palau': 'PW',
                   'puerto rico': 'PR',
                   'u.s. virgin islands': 'VI',
                   'us armed forces europe': 'AE',
                   'us armed forces americas': 'AA',
                   'us armed forces pacific': 'AP'}
    if state not in state_codes.values():
        state = state_codes.get(state.lower(), 'undefined')
    return state


def create_officer(first, middle, last, amount):
    '''Creates a highlyCompensatedOfficer element'''
    officer = award_schema.highlyCompensatedOfficer()
    officer.highlyCompensatedOfficerFirstName = write_string(first)
    officer.highlyCompensatedOfficerMiddleInitial = write_string(middle)
    officer.highlyCompensatedOfficerLastName = write_string(last)
    officer.highlyCompensatedOfficerCompensation = write_amount(amount)
    return officer


def create_award(data):
    '''Creates an award element'''
    award = finassist.award()
    award.awardDescription = write_string(data.get('AwardDescription'))
    award.awardID = write_string(data.get('FainAwardNumber'))
    award.parentAwardID = write_string('TODO')
    award.modificationAmendmentNumber = write_string(data.get('AwardModAmendmentNumber'))
    award.recordType = award_schema.recordType(get_or_undefined(data, 'RecordType'), contextRef='ID2')
    award.typeOfAction = award_schema.typeOfAction(get_or_undefined(data, 'TypeOfAction'), contextRef='ID2')
    # TODO: Figure out type of transaction
    award.typeOfTransactionCode = award_schema.typeOfTransactionCode('undefined', contextRef='ID2')
    award.awardeeInformation = finassist.awardeeInformation()
    award.awardeeInformation.businessType = award_schema.businessType(get_or_undefined(data, 'BusinessType'), contextRef='ID2')
    award.awardeeInformation.awardeeLegalBusinessName = write_string(data.get('RecipientLegalEntityName'))
    award.awardeeInformation.ultimateParentUniqueIdentifier = write_int(data.get('RecipientUltimateParent1Id'))
    award.awardeeInformation.awardeeUniqueIdentifier = write_int(data.get('RecipientDunsNumber'))
    award.awardeeInformation.awardeeUniqueIdentifierSupplemental = write_string()
    award.awardeeInformation.ultimateParentLegalBusinessName = write_string(data.get('RecipientUltimateParentLegalEntityName'))
    award.awardeeInformation.awardeeAddress = gen.address()
    award.awardeeInformation.awardeeAddress.streetAddress = gen.streetAddress()
    award.awardeeInformation.awardeeAddress.streetAddress.streetAddressLine.append(write_string(data.get('RecipientLegalEntityAddressStreet1')))
    award.awardeeInformation.awardeeAddress.city = write_string(data.get('RecipientLegalEntityCityName'))
    award.awardeeInformation.awardeeAddress.county = write_string()
    award.awardeeInformation.awardeeAddress.state = gen.state(fix_state(get_or_undefined(data, 'RecipientLegalEntityStateCode')), contextRef='ID2')
    award.awardeeInformation.awardeeAddress.postalCode = write_string(data.get('RecipientLegalEntityPostalCode'))
    award.awardeeInformation.awardeeAddress.zipCodePlus4 = write_string(data.get('RecipientLegalEntityZip+4'))
    award.awardeeInformation.awardeeAddress.countryName = write_string(data.get('RecipientLegalEntityCountryName'))
    award.awardeeInformation.awardeeAddress.countryCode = write_string(data.get('RecipientLegalEntityCountryCode'))
    #award.awardeeInformation.awardeeAddress.congressionalDistrict = gen.congressionalDistrict(get_or_undefined(data, 'RecipientLegalEntityCongressionalDistrict'), contextRef='ID2')
    award.primaryPlaceOfPerformance = gen.address()
    award.primaryPlaceOfPerformance.streetAddress = gen.streetAddress()
    award.primaryPlaceOfPerformance.streetAddress.streetAddressLine.append(write_string())
    award.primaryPlaceOfPerformance.city = write_string(data.get('PlaceOfPerfCity'))
    award.primaryPlaceOfPerformance.county = write_string(data.get('PlaceOfPerfCounty'))
    award.primaryPlaceOfPerformance.state = gen.state(fix_state(get_or_undefined(data, 'PlaceOfPerfState')), contextRef='ID2')
    award.primaryPlaceOfPerformance.postalCode = write_string()
    award.primaryPlaceOfPerformance.zipCodePlus4 = write_string(data.get('PlaceOfPerfZip+4'))
    award.primaryPlaceOfPerformance.countryName = write_string(data.get('PlaceOfPerfCountryName'))
    award.primaryPlaceOfPerformance.countryCode = write_string()
    #award.primaryPlaceOfPerformance.congressionalDistrict = gen.congressionalDistrict(get_or_undefined(data, 'PlaceOfPerfCongressionalDistrict'), contextRef='ID2')
    award.periodOfPerformance = finassist.periodOfPerformance()
    award.periodOfPerformance.periodOfPerformanceActionDate = create_date(data.get('ActionDateYear'), data.get('ActionDateMonth'), data.get('ActionDateDay'))
    award.periodOfPerformance.periodOfPerformanceStartDate = create_date(data.get('PeriodOfPerfStartYear'), data.get('PeriodOfPerfStartMonth'), data.get('PeriodOfPerfStartDay'))
    award.periodOfPerformance.periodOfPerformanceCurrentEndDate = create_date(data.get('PeriodOfPerfCurrentEndYear'), data.get('PerioOfPerfCurrentEndMonth'), data.get('PeriodOfPerfCurrentEndDay'))
    award.periodOfPerformance.periodOfPerformancePotentialEndDate = create_date(data.get('PeriodOfPerfPotentialEndYear'), data.get('PeriodOfPerfPotentialEndMonth'), data.get('PeriodOfPerfPotentialEndDay'))
    award.awardingAgency.append(create_agency(data.get('AwardingAgencyCode'), data.get('AwardingAgencyName'), data.get('AwardingOfficeName'),data.get('AwardingOfficeCode')))
    award.fundingAgency.append(create_agency(data.get('FundingAgencyCode'), data.get('FundingAgencyName'), data.get('FundingOfficeName'), data.get('FundingOfficeCode')))
    award.awardingSubTierAgency.append(create_agency(data.get('AwardingSubTierAgencyCode'), data.get('AwardingSubTierAgencyName'), '', ''))
    award.fundingSubTierAgency.append(create_agency(data.get('FundingSubTierAgencyCode'), data.get('FundingSubTierAgencyName'), '', ''))
    award.highlyCompensatedOfficer.append(create_officer(data.get('HighCompOfficer1FirstName'), data.get('HighCompOfficer1MiddleInitial'), data.get('HighCompOfficer1LastName'), data.get('HighCompOfficer1Amount')))
    award.highlyCompensatedOfficer.append(create_officer(data.get('HighCompOfficer2FirstName'), data.get('HighCompOfficer2MiddleInitial'), data.get('HighCompOfficer2LastName'), data.get('HighCompOfficer2Amount')))
    award.highlyCompensatedOfficer.append(create_officer(data.get('HighCompOfficer3FirstName'), data.get('HighCompOfficer3MiddleInitial'), data.get('HighCompOfficer3LastName'), data.get('HighCompOfficer3Amount')))
    award.highlyCompensatedOfficer.append(create_officer(data.get('HighCompOfficer4FirstName'), data.get('HighCompOfficer4MiddleInitial'), data.get('HighCompOfficer4LastName'), data.get('HighCompOfficer4Amount')))
    award.highlyCompensatedOfficer.append(create_officer(data.get('HighCompOfficer5FirstName'), data.get('HighCompOfficer5MiddleInitial'), data.get('HighCompOfficer5LastName'), data.get('HighCompOfficer5Amount')))
    award.catalogOfFederalDomesticAssistanceProgram = finassist.catalogOfFederalDomesticAssistanceProgram()
    award.catalogOfFederalDomesticAssistanceProgram.catalogOfFederalDomesticAssistanceTitle = write_string(data.get('CFDA_Description'))
    award.catalogOfFederalDomesticAssistanceProgram.catalogOfFederalDomesticAssistanceNumber = write_string(data.get('CFDA_Code'))
    award.awardAmounts = finassist.awardAmounts()
    award.awardAmounts.federalFundingAmount = write_amount()
    award.awardAmounts.totalFundingAmount = write_amount(data.get('CurrentTotalFundingObligationAmount'))
    award.awardAmounts.nonFederalFundingAmount = write_amount(data.get('NonFederalFundingAmount'))
    return award


def create_USSGL_header(indexed_af, approp):
    tas = create_tas(approp)
    header = ussgl.USSGLentryHeader()
    header.treasuryAccountSymbol = create_tas_element(approp)
    # TODO: Wrong level of aggregation?
    header.obligatedAmount = write_amount()
    header.unobligatedAmount = write_amount(approp.get('UnobligatedAmount'))
    header.budgetAuthorityAppropriated = write_amount(approp.get('BudgetAuthorityAppropriatedAmount'))
    header.otherBudgetaryResources = write_amount(approp.get('OtherBudgetaryResourcesAmount'))
    # TODO: Wrong level of aggregation?
    header.outlays = write_amount()
    # TODO: Necessary?
    header.appropriationAccount = write_string()
    for af in indexed_af[tas]:
        header.entryDetail.append(create_entry_detail(af))
    return header


def create_entry_detail(single_af):
    entry = ussgl.entryDetail()
    entry.account = ussgl.account()
    entry.account.accountNumber = write_string(single_af.get('MainAccountCode'))
    entry.account.objectClass = write_string(single_af.get('ObjectClass'))
    entry.account.awardID = write_string(single_af.get('FainAwardNumber'))
    # TODO: Are these still needed?
    entry.account.accountDescription = write_string('')
    entry.amount = write_amount()
    entry.debitCreditCode = gen.debitCreditCodeItemType('undefined', contextRef='ID2')
    entry.beginningEndIndicator = ussgl.beginningEndIndicatorItemType('E', contextRef='ID2')
    # TODO: Wrong level of aggregation?
    entry.programActivity = write_string('')
    return entry


def create_accounting(approps, af):
    result = ussgl.accountingEntries()
    result.fiscalYear = write_string('2014')
    result.period = write_string('FY')
    indexed_af = index_by_tas(af)
    for approp in approps:
        result.USSGLentryHeader.append(create_USSGL_header(indexed_af, approp))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts four csv files into XBRL')
    parser.add_argument('appropriation', help='Appropriation CSV')
    parser.add_argument('object_class', help='Object Class CSV')
    parser.add_argument('award_financial', help='Award Financial CSV')
    parser.add_argument('award', help='Award CSV')
    parser.add_argument('output_dir', help='Output directory')

    args = parser.parse_args()

    with codecs.open(args.award) as f:
        awards = [row for row in csv.DictReader(f)]
    with codecs.open(args.appropriation) as f:
        appropriation = [row for row in csv.DictReader(f)]
    with codecs.open(args.object_class) as f:
        ocpa = [row for row in csv.DictReader(f)]
    with codecs.open(args.award_financial) as f:
        award_financial = [row for row in csv.DictReader(f)]

    output_dir = args.output_dir
    if output_dir[:-1] != '/':
        output_dir += '/'
    try:
        os.mkdir(output_dir)
    except:
        pass
    awards_xml = {award['FainAwardNumber']: create_award(award).toDOM().toprettyxml() for award in awards}
    accounting_xml = create_accounting(appropriation, award_financial).toDOM().toprettyxml()
    with codecs.open(output_dir + 'accounting.xml', 'w', 'utf-8') as f:
        f.write(accounting_xml)
    for key in awards_xml:
        with codecs.open(output_dir + key + '.xml', 'w', 'utf-8') as f:
            f.write(awards_xml[key])
