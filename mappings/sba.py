

def getNonFederalFundingAmount(record):
    #prism fields
    amount = 0
    fields = ['grantheader.sba1222personalservicenf', 'grantheader.sba1222fringebenefitsnf', 'grantheader.sba1222consultantsnf', 'grantheader.sba1222travelnf', 'grantheader.sba1222equipmentnf', 'grantheader.sba1222suppliesnf', 'grantheader.sba1222contractualnf', 'grantheader.sba1222othernf', 'grantheader.sba1222indcostnf', 'grantheader.sba1222othercostnf']

    for f in fields: amount += record[f]
    return f

def getFundingOfficeName(record):
    return record['itemacct.acctfield3'] + record['addr.name']

def getObligatedAmount(record):
    return record['po_lines_all.quantity'] * record['po_lines_all.unit_price']

schema_map = {

    #fields from awardee message
    'award.awardee.businessName': 'docvendor.Name',
    'award.awardee.DUNSNumber': 'docvendor.duns',
    'award.awardee.DUNSPlusFour': 'docvendor.DUNSPLUS4',
    'award.awardee.parentDUNSNumber': None,
    'award.awardee.parentBusinessName': None,
    'award.awardee.businessCongressionalDistrict': 'grantheader.sba1222congdistno',
    'award.awardee.businessType': None,
    'award.awardee.highlyCompensatedOfficer': None,
    'award.awardee.businessCongressionalDistrict': None,

    #fields from address message
    'award.awardee.businessAddress.street1': 'docvendor.address1',
    'award.awardee.businessAddress.street2': 'ap_supplier_sites.address2',
    'award.awardee.businessAddress.street3': 'ap_supplier_sites.address3',
    'award.awardee.businessAddress.city': 'ap_supplier_sites.city',
    'award.awardee.businessAddress.state': 'ap_supplier_sites.state',
    'award.awardee.businessAddress.postalCode': 'ap_supplier_sites.zip',
    'award.awardee.businessAddress.USZopCodePlusFour': 'ap_supplier_sites.zip',
    'award.awardee.businessAddress.countryName': 'grantheader.recipientcountryname', #was changed to NA in subsequent SBA mapping
    'award.awardee.businessAddress.countryCode': 'grantheader.recipientcountrycode', #was changed to NA in subsequent SBA mapping

    #fields from award message
    'award.fundingActionObligation.amount': getObligatedAmount, #'header.obligatedamt', #prism, is table name correct?
    'award.fundingActionObligation.currency': 'USD', #assuming all SBA is in US Dollars
    'award.nonFederalFundingAmount.amount': getObligatedAmount, #getNonFederalFundingAmount,  #changed in subsequent SBA mapping
    'award.nonFederalFundingAmount.currency': 'USD',
    'award.currentTotalFundingObligationAmount.amount': getObligatedAmount, #'header.obligatedamt',
    'award.currentTotalFundingObligationAmount.currency': 'USD',
    'award.currentTotalValue.amount': getObligatedAmount, #'header.amount',
    'award.currentTotalValue.currency': 'USD',
    'award.potentialTotalValue.amount': getObligatedAmount, #'header.amount',
    'award.potentialTotalValue.currency': 'USD',
    'award.typeOfTransactionCode': 'po_distributions_all.attribute_category', #'header.awardtype', #MISSING from proto files, or named differently (line 21 in sba mapping excel)
    'award.fundingAgency.agencyName': 'Small Business Administration',
    'award.fundingAgency.agencyCode': 'SBA', # is this right?
    'award.fundingAgency.subTierAgencyName': 'Small Business Administration',
    'award.fundingAgency.subTierAgencyCode': 'SBA',
    'award.fundingAgency.officeName': 'gl_code_combinations.segment3', #getFundingOfficeName,
    'award.fundingAgency.officeCode': 'fnd_flex_values_vl', #'itemacct.acctfield3',
    'award.NAICSCode': 'naicssicdata.naics', #prism, was changed to NA in subsequent mapping
    'award.NAICSCodeDescription':  'naicssicdata.descr', #prism, was changed to NA in subsequent mapping
    'award.CFDAProgramNumber': 'header.cfdanumber', #prism, was changed to NA in subsequent mapping

    'award.CFDAProgramTitle': None, #in their main CFDA table, not in the data they sent us. We could reference using the program number though, was changed to NA in subsequent mapping

    
    #on AgencyTransaction message
    'treasuryAccountSymbol': None, #jaams
    
    


}
