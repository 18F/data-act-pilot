import pandas as pd
import numpy as np
import glob, argparse
pd.options.mode.chained_assignment = None

def read_data(data_dir):
    # read all .txt files in specified directory
    # return a dictionary of pandas DataFrames
    files = glob.glob('data/{}/*.txt'.format(data_dir))
    df_dict = {}
    for file in files:
        key = file.split('/')[-1][:-4].lower()
        df_dict[key] = pd.read_csv(file)
        rows = len(df_dict[key].index)
        df_dict[key].rename(
            columns=lambda x: '{}.'.format(key) + x.lower(), inplace = True)
        print('Read {} records from {}'.format(
            rows, file))
    return df_dict

def join_data(df1, df2, key1, key2):
    #return joined databframes (full join)
    print('Joining {} ({} rows) to {} ({} rows)'.format(
        key2, len(df2.index), key1, len(df1.index)))
    joined = pd.merge(
        df1, df2, left_on = key1, right_on = key2)
    print('Joined rows = {}\n'.format(len(joined.index)))
    return joined

def run():

    parser = argparse.ArgumentParser(description="Read exports from SBA financial and award systems and write out combined file in DATA Act format")
    parser.add_argument('-o', dest='outfile', help='the .csv file that contains the combined data')

    args = parser.parse_args()
    outfile = args.outfile

    jp_merge = pd.DataFrame
    jaams = read_data('jaams')
    prism = read_data('prism')

    #join prism award numbers to jaams award numbers
    print('\nUnique award numbers in JAAMS po_headers_all: {}'.format(
        len(jaams['po_headers_all']['po_headers_all.segment1'])))
    jp_merge = join_data(
            jaams['po_headers_all'],
            prism['header'],
            ['po_headers_all.segment1'],
            ['header.docnum'])

    jp_merge = join_data(
        jp_merge,
        prism['grantheader'],
        ['header.dockey', 'header.verkey'],
        ['grantheader.dockey', 'grantheader.verkey']
    )

    jp_merge = join_data(
        jp_merge,
        prism['docvendor'],
        ['header.dockey', 'header.verkey'],
        ['docvendor.dockey', 'docvendor.verkey']
    )

    jp_merge = join_data(
        jp_merge, prism['item'],
        ['header.dockey', 'header.verkey'],
        ['item.hdrdockey', 'item.hdrverkey']
    )

    jp_merge = join_data(
        jp_merge, prism['deliverylocdate'],
        ['item.dockey', 'item.verkey'],
        ['deliverylocdate.dockey', 'deliverylocdate.verkey'])

    jp_merge = join_data(
        jp_merge, prism['itemacct'],
        ['deliverylocdate.deliverylocdatekey'],
        ['itemacct.deliverylocdatekey']
    )

    jp_merge= pd.merge(
        jp_merge, prism['naicssicdata'],
        left_on = 'header.primarysiccode',
        right_on = 'naicssicdata.naics',
        how = 'left' #left join b/c NAICS not always applicable?
    )

    jp_merge = join_data(
        jp_merge, jaams['ap_supplier_sites_all'],
        ['po_headers_all.vendor_id', 'po_headers_all.vendor_site_id'],
        ['ap_supplier_sites_all.vendor_id', 'ap_supplier_sites_all.vendor_site_id'] 
    )

    jp_merge = join_data(
        jp_merge, jaams['po_lines_all'],
        ['po_headers_all.po_header_id'],
        ['po_lines_all.po_header_id']
    )

    jp_merge = join_data(
        jp_merge, jaams['po_distributions_all'],
        ['po_lines_all.po_header_id', 'po_lines_all.po_line_id'],
        ['po_distributions_all.po_header_id', 'po_distributions_all.po_line_id']
    )

    jp_merge = join_data(
        jp_merge, jaams['gl_code_combinations'],
        'po_distributions_all.code_combination_id',
        'gl_code_combinations.code_combination_id'
    )

    fv_fund_parameters = jaams['fv_fund_parameters']
    fv_treasury_symbols = jaams['fv_treasury_symbols']
    jp_merge = pd.merge(
        pd.merge(fv_fund_parameters, fv_treasury_symbols, 
        left_on = 'fv_fund_parameters.treasury_symbol_id',
        right_on = 'fv_treasury_symbols.treasury_symbol_id'),
        jp_merge,
        left_on = 'fv_fund_parameters.fund_value',
        right_on = 'gl_code_combinations.segment2'
    )
    
    jp_merge = join_data(
        jp_merge, prism['association'],
        ['header.dockey', 'header.verkey'],
        ['association.dockey', 'association.verkey']
    )
    #then use Association as the crosswalk
    jp_merge = join_data(
        jp_merge, prism['faadsciv'],
        ['association.assocdockey', 'association.assocverkey'],
        ['faadsciv.dockey', 'faadsciv.verkey']
    )

    jp_merge = join_data(
        jp_merge, prism['docaddr'],
        ['header.issuingdocaddresskey'],
        ['docaddr.docaddrkey'])
    
    #hard-coded agency values
    jp_merge['funding_agency_name'] = 'Small Business Administration'
    jp_merge['funding_agency_code'] = '73'
    jp_merge['funding_sub_tier_agency_name'] = 'Small Business Administration'
    jp_merge['funding_sub_tier_agency_code'] = '73'
    jp_merge['awarding_agency_name'] = 'Small Business Administration'
    jp_merge['awarding_agency_code'] = '73'
    jp_merge['awarding_sub_tier_agency_name'] = 'Small Business Administration'
    jp_merge['awarding_sub_tier_agency_code'] = '73'


    #reduce the joined data to fields needed for the data act schema
    jp_merge = jp_merge.drop_duplicates()
    data_act = jp_merge[[
        'po_headers_all.segment1', #award id
        'header.versionnum', #award modification
        'header.docnum',
        'header.verkey',
        'po_lines_all.item_description', #award description
        #'header.shortdescr', #award description
        'header.awarddate', #action date
        'docvendor.name', #Recipient name
        'po_distributions_all.attribute10', #period of performance start date
        #'header.startdate', #period of performance start date
        'po_distributions_all.attribute11', #period of performance end date
        #'header.enddate', #period of performance end date
        'docvendor.duns', #awardee/recipient legal business DUNS
        'docvendor.dunsplus4', #awardee/recipient legal business DUNS+4
        'docvendor.address1', #awardee/recipient legal business street address line 1
        'docvendor.address2', #awardee/recipient legal busines street address line 2
        'docvendor.address3', #awardee/recipient legal business street address line 3
        'docvendor.city', #awardee/recipient legal business city
        'docvendor.state', #awardee/recipient state
        'docvendor.zip', #awardee/recipient us zip code + 4; awardee/recipient postal code
        'header.amount', #current total value of award/potential total value of award
        'header.awardtype', #type of award
        'faadsciv.assistancetranstype', #type of transaction code
        'header.primarysiccode', #naics code
        'grantheader.sba1222countyname', #recipient county name
        'grantheader.sba1222countycode', #recipient county code
        'grantheader.recipientcountrycode', #awardee/recipient legal business country code
        'grantheader.recipientcountryname', #awardee/recipient legal business country name
        'grantheader.sba1222personalservicenf', #used for non-fed funding amt calculation
        'grantheader.sba1222fringebenefitsnf', #used for non-fed funding amt calculation
        'grantheader.sba1222consultantsnf', #used for non-fed funding amt calculation
        'grantheader.sba1222travelnf', #used for non-fed funding amt calculation
        'grantheader.sba1222equipmentnf', #used for non-fed funding amt calculation
        'grantheader.sba1222suppliesnf', #used for non-fed funding amt calculation
        'grantheader.sba1222contractualnf', #used for non-fed funding amt calculation
        'grantheader.sba1222othernf', #used for non-fed funding amt calculation
        'grantheader.sba1222indcostnf', #used for non-fed funding amt calculation
        'grantheader.sba1222othercostnf', #used for non-fed funding amt calculation
        #'fv_treasury_symbols.treasury_symbol', #TAS
        'itemacct.tas#', #TAS
        'po_lines_all.quantity',
        'po_lines_all.unit_price',
        'funding_agency_name', #funding agency name
        'funding_agency_code', #funding agency code
        'funding_sub_tier_agency_name', #funding sub-tier agency name
        'funding_sub_tier_agency_code', #funding sub-tier agency code
        'po_distributions_all.attribute_category', #type of award code
        'header.obligatedamt', #amount of ba appropriated; obligation
        'po_distributions_all.quantity_billed', #outlay
        'gl_code_combinations.segment3', #funding office name
        'itemacct.acctfield3', #funding office name and funding office code
        'gl_code_combinations.segment5', #object class woo!
        #'itemacct.acctfield5', #object class
        #'gl_code_combinations.code_combination_id', #appropriations account
        'itemacct.acctfield6', #appropriations account
        'gl_code_combinations.segment4', #program activity
        #'itemacct.acctfield4', #program activity
        'grantheader.sba1222congdistno', #place of performance congressional district
        'faadsciv.recordtype', #record type
        'faadsciv.countycityname', #primary place of performance county name/primary place of performance city
        'faadsciv.countycitycode', #primary place of performance county code
        'faadsciv.principalstatecode', #primary place of performance state code
        'faadsciv.principalstatename', #primary place of performance state name
        'faadsciv.placeofperfzip', #primary place of performance zip code + 4
        'faadsciv.placeofperfcountrycode', #primary location of performance country code
        'faadsciv.placeofperfcountryname', #primary location of performance country name
        'faadsciv.cfdaprogramnumber', #cfda program number
        'faadsciv.cfdaprogramtitle', #cfda program title
        'docaddr.name', #awarding office name
        'header.issuingdocaddresskey', #awarding office code
        'faadsciv.recipienttype', #recipient type
        'funding_agency_name',
        'funding_agency_code',
        'funding_sub_tier_agency_name',
        'funding_sub_tier_agency_code',
        'awarding_agency_name',
        'awarding_agency_code',
        'awarding_sub_tier_agency_name',
        'awarding_sub_tier_agency_code'
        ]]

    #write out the data act file
    if not outfile:
        outfile = 'data/data_act.csv'
    data_act.to_csv(outfile, index = False)
    print('DATA Act combined file written to {}'.format(outfile))

run()
