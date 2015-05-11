

def getNonFederalFundingAmount(record):
    #prism fields
    amount = 0
    fields = ['grantheader.sba1222personalservicenf', 'grantheader.sba1222fringebenefitsnf', 'grantheader.sba1222consultantsnf', 'grantheader.sba1222travelnf', 'grantheader.sba1222equipmentnf', 'grantheader.sba1222suppliesnf', 'grantheader.sba1222contractualnf', 'grantheader.sba1222othernf', 'grantheader.sba1222indcostnf', 'grantheader.sba1222othercostnf']

    for f in fields: amount += float(record[f])
    return f

def getFundingOfficeName(record):
    return record['itemacct.acctfield3'] + record['addr.name']

def getObligatedAmount(record):
    return float(record['po_lines_all.quantity']) * float(record['po_lines_all.unit_price'])

schema_map = {

    #fields from awardee message
    'award.awardees[0].businessName': 'docvendor.Name',
    'award.awardees[0].DUNSNumber': 'docvendor.duns',
    'award.awardees[0].DUNSPlusFour': 'docvendor.DUNSPLUS4',
    'award.awardees[0].parentDUNSNumber': None,
    'award.awardees[0].parentBusinessName': None,
    'award.awardees[0].businessCongressionalDistrict': 'grantheader.sba1222congdistno',
    'award.awardees[0].businessType': None,
    'award.awardees[0].highlyCompensatedOfficer': None,

    #fields from address message
    'award.awardees[0].recipientType': 'vendor2.businesstype',
    'award.awardees[0].businessName': 'docvendor.name', 
    'award.awardees[0].businessAddress.street1': 'ap_supplier_sites_all.address1',
    'award.awardees[0].businessAddress.street2': 'ap_supplier_sites_all.address2',
    'award.awardees[0].businessAddress.street3': 'ap_supplier_sites_all.address3',
    'award.awardees[0].businessAddress.city': 'ap_supplier_sites_all.city',
    'award.awardees[0].businessAddress.state': 'ap_supplier_sites_all.state',
    'award.awardees[0].businessAddress.postalCode': 'ap_supplier_sites_all.zip',
    'award.awardees[0].businessAddress.USZipCodePlusFour': 'ap_supplier_sites_all.zip',
    'award.awardees[0].businessAddress.countryName': 'grantheader.recipientcountryname', #was changed to NA in subsequent SBA mapping
    'award.awardees[0].businessAddress.countryCode': 'grantheader.recipientcountrycode', #was changed to NA in subsequent SBA mapping

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
    'award.fundingAgency.agencyCode': 73, # is this right?
    'award.fundingAgency.subTierAgencyName': 'Small Business Administration',
    'award.fundingAgency.subTierAgencyCode': 73,
    'award.fundingAgency.officeName': 'gl_code_combinations.segment3', #getFundingOfficeName,
    'award.fundingAgency.officeCode': 'fnd_flex_values_vl', #'itemacct.acctfield3',
    
    'award.awardingAgency.officeName': 'docaddr.name',
    'award.awardingAgency.officeCode': 'header.issuingdocaddresskey',
    

    'award.NAICSCode': 'naicssicdata.naics', #prism, was changed to NA in subsequent mapping
    'award.NAICSCodeDescription':  'naicssicdata.descr', #prism, was changed to NA in subsequent mapping
    'award.CFDAProgramNumber': 'faadsciv.cfdaprogramnumber', #prism, was changed to NA in subsequent mapping
    'award.CFDAProgramTitle': 'faadsciv.cfdaprogramtitle', #in their main CFDA table, not in the data they sent us. We could reference using the program number though, was changed to NA in subsequent mapping
    
    'award.awardDescription': 'po_lines_all.item_description',
    'award.awardNumber': 'po_headers_all.segment1',
    'award.actionDate': 'header.awarddate',
    'award.periodOfPerformanceStart': 'po_distributions_all.attribute10',
    'award.periodOfPerformanceCurrentEnd': 'po_distributions_all.attribute11',
    'award.periodOfPerformancePotentialEnd': 'po_distributions_all.attribute11',


    #on AgencyTransaction message
    'transaction.treasuryAccountSymbol.mainAccount': 'itemacct.tas#', #jaams
    'transaction.treasuryAccountSymbol.subAccount': 'gl_code_combinations.code_combination_id',
    'transaction.objectClass': 'gl_code_combinations.segment5',
    'transaction.programActivity': 'gl_code_combinations.segment4', 

    #on Action
    'recordType': 'faadsciv.recordtype',
    


}
