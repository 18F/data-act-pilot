import pandas as pd
import numpy as np
import glob, argparse
pd.options.mode.chained_assignment = None

def read_data(data_dir):
    """returns all .txt files in specified directory as a dict of DataFrames"""
    files = glob.glob('data/{}/*.txt'.format(data_dir))
    df_dict = {}
    for file in files:
        key = file.split('/')[-1][:-4].lower()
        df_dict[key] = pd.read_csv(
            file,
            dtype = {
                'DUNS': np.object,
                'DUNSPLUS4': np.object,
                'CFDAPROGRAMNUMBER': np.object,
                'ZIP': np.object,
                'SBA122CONGDISTNO': np.object,
                'RECIPIENTCOUNTRYCODE': np.object,
                'ASSISTANCETRANSTYPE': np.object,
                'PRIMARYSICCODE': np.object,
                'TAS#': np.object,
                'SEGMENT1': np.object,
                'VERSIONNUM': np.object,
                'ISSUINGDOCADDRESSKEY': np.object,
                'DOCADDRKEY': np.object,
                'PLACEOFPERFZIP': np.object,
                'PLACEOFPERFCOUNTRYCODE': np.object,
                'RECIPIENTTYPE': np.object,
                'ACCTFIELD6': np.object,
                'PO_HEADER_ID': np.object,
                'PO_LINE_ID': np.object,
                'PO_DISTRIBUTION_ID': np.object,
                'CODE_COMBINATION_ID': np.object,
                'SEGMENT3': np.object,
                'SEGMENT4': np.object,
                'SEGMENT5': np.object,
                'SEGMENT6': np.object,
                'AE_HEADER_ID': np.object,
                'AE_LINE_NUM': np.object,
                'SOURCE_DISTRIBUTION_ID_NUM_1': np.object,
                'INVOICE_ID': np.object,
                'LINE_NUMBER': np.object,
                'INVOICE_LINE_NUMBER': np.object,
                'INVOICE_DISTRIBUTION_ID': np.object,
                'DISTRIBUTION_ID': np.object
            }
        )
        rows = len(df_dict[key].index)
        df_dict[key].rename(
            columns=lambda x: '{}.'.format(key) + x.lower(), inplace = True)
        print('Read {} records from {}'.format(
            rows, file))
    return df_dict

def join_data(df1, df2, key1, key2):
    """joins two dataframes and returns the merged output"""
    joined = pd.merge(
        df1, df2, left_on = key1, right_on = key2)
    return joined

def get_value(row):
    """adjust sign of subledger credit/debit"""
    credit = row['xla_ae_lines.accounted_cr']
    debit = row['xla_ae_lines.accounted_dr']
    if pd.isnull(debit):
        return credit
    else:
        return debit * -1

def prep_financial():
    """merge financial data from JAAMS"""
    jaams = read_data('jaams')

    #crosswalk (VERY rough cut) between subledger data and DATA Act elements
    sgl_crosswalk = pd.read_csv(
        'data/other/sgl_account_element_crosswalk.csv',
        dtype = {'code' : np.object}
    )
    #create subledger dataframe
    sgl = join_data(
        jaams['xla_distribution_links'],
        jaams['xla_ae_lines'],
        ['xla_distribution_links.ae_header_id',
            'xla_distribution_links.ae_line_num'],
        ['xla_ae_lines.ae_header_id', 'xla_ae_lines.ae_line_num']
    )
    #merge in code combination lookup for SGL account
    sgl = join_data(
        sgl,
        jaams['gl_code_combinations'],
        ['xla_ae_lines.code_combination_id'],
        ['gl_code_combinations.code_combination_id']
    )
    sgl = sgl.rename(
        columns = {
            'gl_code_combinations.segment6' : 'gl_code_combinations.sgl_account'
        }
    )
    sgl = join_data(
        sgl,
        sgl_crosswalk,
        ['gl_code_combinations.sgl_account'],
        ['sgl_account']
    )
    sgl = sgl[['xla_ae_lines.ae_header_id',
       'xla_ae_lines.ae_line_num',
       'xla_ae_lines.accounted_dr',
       'xla_ae_lines.accounted_cr',
       'xla_distribution_links.source_distribution_id_num_1',
       'xla_distribution_links.source_distribution_type',
       'gl_code_combinations.sgl_account',
        'data_act_element',
        'code_description']]

    # Create PO dataframe
    po = pd.DataFrame()
    po = join_data(
        jaams['po_headers_all'][['po_headers_all.po_header_id',
            'po_headers_all.segment1']],
        jaams['po_lines_all'][['po_lines_all.po_header_id',
            'po_lines_all.po_line_id', 'po_lines_all.item_description',
            'po_lines_all.quantity','po_lines_all.unit_price']],
        ['po_headers_all.po_header_id'],
        ['po_lines_all.po_header_id']
        )
    po = join_data(
        po,
        jaams['po_line_locations_all'][['po_line_locations_all.po_line_id']],
        ['po_lines_all.po_line_id'],
        ['po_line_locations_all.po_line_id']
    )
    po = join_data(
        po,
        jaams['po_distributions_all'][['po_distributions_all.po_distribution_id',
            'po_distributions_all.po_header_id',
            'po_distributions_all.po_line_id',
            'po_distributions_all.code_combination_id',
            'po_distributions_all.attribute10',
            'po_distributions_all.attribute11',
            'po_distributions_all.attribute_category',
            'po_distributions_all.quantity_billed',
            'po_distributions_all.req_distribution_id']],
        ['po_lines_all.po_line_id'],
        ['po_distributions_all.po_line_id']
    )
    po = join_data(
        po,
        jaams['gl_code_combinations'],
        ['po_distributions_all.code_combination_id'],
        ['gl_code_combinations.code_combination_id']
    )
    po = join_data(
        po,
        sgl[sgl['xla_distribution_links.source_distribution_type'] == 'PO_DISTRIBUTIONS_ALL'],
        ['po_distributions_all.po_distribution_id'],
        ['xla_distribution_links.source_distribution_id_num_1']
    )
    #grab TAS
    po = join_data(
        po,
        jaams['fv_fund_parameters'],
        ['gl_code_combinations.segment2'],
        ['fv_fund_parameters.fund_value']
    )
    po = join_data(
        po,
        jaams['fv_treasury_symbols'],
        ['fv_fund_parameters.treasury_symbol_id'],
        ['fv_treasury_symbols.treasury_symbol_id']
    )

    #tidy up
    po = po[['po_headers_all.po_header_id',
        'po_lines_all.po_line_id',
        'po_distributions_all.po_distribution_id',
        'po_distributions_all.req_distribution_id',
        'po_headers_all.segment1', #award number
        'po_lines_all.item_description',
        'po_lines_all.quantity',
        'po_lines_all.unit_price',
        'po_distributions_all.quantity_billed',
        'po_distributions_all.code_combination_id',
        'po_distributions_all.attribute10', #period of performance start dt
        'po_distributions_all.attribute11', #period of performance end dt
        'gl_code_combinations.segment3', #funding office
        'gl_code_combinations.segment4', #program activity
        'gl_code_combinations.segment5', #object class
        'fv_treasury_symbols.treasury_symbol', #tas
        'xla_ae_lines.ae_header_id',
        'xla_ae_lines.ae_line_num',
        'xla_ae_lines.accounted_dr',
        'xla_ae_lines.accounted_cr',
        'gl_code_combinations.sgl_account',
        'data_act_element',
        'code_description'
        ]]
    po['tas'] = (po['fv_treasury_symbols.treasury_symbol'].str[:2] +
        po['fv_treasury_symbols.treasury_symbol'].str[-4:])

    #combine debits and credits into a single columns
    po['xla_ae_lines.accounted_amt'] = (
        po.apply(lambda row: get_value(row),axis=1))

    #aggregate
    po_agg = pd.pivot_table(po,
        index=['po_headers_all.po_header_id',
        'po_lines_all.po_line_id',
        'po_distributions_all.po_distribution_id',
        'po_distributions_all.req_distribution_id',
        'po_headers_all.segment1',
        'po_lines_all.item_description',
        'xla_ae_lines.ae_header_id',
        'xla_ae_lines.ae_line_num',
        'po_distributions_all.attribute10', #period of performance start dt
        'po_distributions_all.attribute11', #period of performance end dt
        'gl_code_combinations.segment3', #funding office
        'gl_code_combinations.segment4', #program activity
        'gl_code_combinations.segment5',
        'fv_treasury_symbols.treasury_symbol',
        'tas'],
        columns = ['data_act_element'],
        values = ['xla_ae_lines.accounted_amt']
    )
    po_agg = po_agg.groupby(
        level=['po_headers_all.po_header_id',
        'po_lines_all.po_line_id',
        'po_distributions_all.po_distribution_id',
        'po_distributions_all.req_distribution_id',
        'po_headers_all.segment1',
        'po_lines_all.item_description',
        'po_distributions_all.attribute10', #period of performance start dt
        'po_distributions_all.attribute11', #period of performance end dt
        'gl_code_combinations.segment3', #funding office
        'gl_code_combinations.segment4', #program activity
        'gl_code_combinations.segment5',
        'fv_treasury_symbols.treasury_symbol',
        'tas']
    ).sum()
    po_agg.columns = po_agg.columns.get_level_values(1)

    # create invoice distributions dataframe
    invd = join_data(
        jaams['ap_invoice_distributions_all'],
        sgl[sgl['xla_distribution_links.source_distribution_type'] == 'AP_INV_DIST'],
        ['ap_invoice_distributions_all.invoice_distribution_id'],
        ['xla_distribution_links.source_distribution_id_num_1']
    )

    #tidy up
    invd = invd[[
        'ap_invoice_distributions_all.po_distribution_id',
        'xla_ae_lines.ae_header_id',
        'xla_ae_lines.ae_line_num',
        'xla_ae_lines.accounted_dr',
        'xla_ae_lines.accounted_cr',
        'data_act_element'
        ]]

    #combine debits and credits into a single columns
    invd['xla_ae_lines.accounted_amt'] = invd.apply(
        lambda row: get_value(row),axis=1)

    #aggregate
    invd_agg = pd.pivot_table(invd,
        index=[
            'ap_invoice_distributions_all.po_distribution_id',
            'xla_ae_lines.ae_header_id',
            'xla_ae_lines.ae_line_num',
        ],
        columns = ['data_act_element'],
        values = ['xla_ae_lines.accounted_amt']
    )
    invd_agg = invd_agg.groupby(
        level=['ap_invoice_distributions_all.po_distribution_id']
        ).sum()
    invd_agg.columns = invd_agg.columns.get_level_values(1)
    invd_agg.reset_index(inplace = True)
    po_agg.reset_index(inplace = True)

    # join this to po distributions
    po_agg = pd.merge(
        po_agg,
        invd_agg,
        left_on = 'po_distributions_all.po_distribution_id',
        right_on = 'ap_invoice_distributions_all.po_distribution_id',
        how = 'left',
        suffixes = ('_po', '_inv')
    )

    # math!
    po_agg['obligated_amt'] = (po_agg['account_obligation_amt_po'] +
        po_agg['account_obligation_amt_inv'])
    po_agg = po_agg.rename(columns = {'account_outlay_amt' : 'outlay_amt'})
    #po_agg.drop(po_agg.columns[[10,11,12,13]],axis = 1, inplace = True)
    return po_agg

def prep_awards():
    """merge awards data from Prism"""
    prism = read_data('prism')

    award_merge = join_data(
        prism['header'],
        prism['grantheader'],
        ['header.dockey', 'header.verkey'],
        ['grantheader.dockey', 'grantheader.verkey']
    )

    award_merge = join_data(
        award_merge,
        prism['docvendor'],
        ['header.dockey', 'header.verkey'],
        ['docvendor.dockey', 'docvendor.verkey']
    )

    award_merge = join_data(
        award_merge, prism['item'],
        ['header.dockey', 'header.verkey'],
        ['item.hdrdockey', 'item.hdrverkey']
    )

    award_merge = join_data(
        award_merge, prism['deliverylocdate'],
        ['item.dockey', 'item.verkey'],
        ['deliverylocdate.dockey', 'deliverylocdate.verkey'])

    award_merge = join_data(
        award_merge, prism['itemacct'],
        ['deliverylocdate.deliverylocdatekey'],
        ['itemacct.deliverylocdatekey']
    )

    award_merge= pd.merge(
        award_merge, prism['naicssicdata'],
        left_on = 'header.primarysiccode',
        right_on = 'naicssicdata.naics',
        how = 'left' #left join b/c NAICS not applicable to grants
    )

    award_merge = join_data(
        award_merge, prism['association'],
        ['header.dockey', 'header.verkey'],
        ['association.dockey', 'association.verkey']
    )

    award_merge = join_data(
        award_merge, prism['faadsciv'],
        ['association.assocdockey', 'association.assocverkey'],
        ['faadsciv.dockey', 'faadsciv.verkey']
    )

    award_merge = join_data(
        award_merge, prism['docaddr'],
        ['header.issuingdocaddresskey'],
        ['docaddr.docaddrkey'])

    #hard-coded agency values
    award_merge['funding_agency_name'] = 'Small Business Administration'
    award_merge['funding_agency_code'] = '73'
    award_merge['funding_sub_tier_agency_name'] = 'Small Business Administration'
    award_merge['funding_sub_tier_agency_code'] = '73'
    award_merge['awarding_agency_name'] = 'Small Business Administration'
    award_merge['awarding_agency_code'] = '73'
    award_merge['awarding_sub_tier_agency_name'] = 'Small Business Administration'
    award_merge['awarding_sub_tier_agency_code'] = '73'

    #a list of the columns that should be in the final file
    award_cols = [
        'header.docnum', #award id
        'header.versionnum', #award modification
        'header.dockey',
        'header.verkey',
        'header.amount', #current total value of award/potential total value of award
        'header.awardtype', #type of award
        'header.primarysiccode', #naics code
        'header.awarddate', #action date
        'header.issuingdocaddresskey', #awarding office code
        'header.shortdescr',
        'grantheader.sba1222countyname', #recipient county name
        'grantheader.sba1222countycode', #recipient county code
        'grantheader.recipientcountrycode', #awardee/recipient legal business country code
        'grantheader.recipientcountryname', #awardee/recipient legal business country name
        'grantheader.sba1222congdistno', #place of performance congressional district
        'docvendor.name', #Recipient name
        'docvendor.duns', #awardee/recipient legal business DUNS
        'docvendor.dunsplus4', #awardee/recipient legal business DUNS+4
        'docvendor.address1', #awardee/recipient legal business street address line 1
        'docvendor.address2', #awardee/recipient legal busines street address line 2
        'docvendor.address3', #awardee/recipient legal business street address line 3
        'docvendor.city', #awardee/recipient legal business city
        'docvendor.state', #awardee/recipient state
        'docvendor.zip', #awardee/recipient us zip code + 4; awardee/recipient postal code
        'docaddr.name', #awarding office name
        'itemacct.acctfield3', #funding office name and funding office code
        'itemacct.acctfield4', #program activity
        'itemacct.acctfield5', #object class
        'itemacct.acctfield6', #appropriations account
        'itemacct.tas#', #TAS
        'itemacct.obligatedamt',
        'faadsciv.recordtype', #record type
        'faadsciv.assistancetranstype', #type of transaction code
        'faadsciv.countycityname', #primary place of performance county name/primary place of performance city
        'faadsciv.countycitycode', #primary place of performance county code
        'faadsciv.principalstatecode', #primary place of performance state code
        'faadsciv.principalstatename', #primary place of performance state name
        'faadsciv.placeofperfzip', #primary place of performance zip code + 4
        'faadsciv.placeofperfcountrycode', #primary location of performance country code
        'faadsciv.placeofperfcountryname', #primary location of performance country name
        'faadsciv.cfdaprogramnumber', #cfda program number
        'faadsciv.cfdaprogramtitle', #cfda program title
        'faadsciv.recipienttype', #recipient type
        'funding_agency_name',
        'funding_agency_code',
        'funding_sub_tier_agency_name',
        'funding_sub_tier_agency_code',
        'awarding_agency_name',
        'awarding_agency_code',
        'awarding_sub_tier_agency_name',
        'awarding_sub_tier_agency_code',
        #add some keys to the file for reference
        'itemacct.deliverylocdatekey',
        'itemacct.itemacctkey'
    ]

    award_merge = award_merge.reset_index(drop=True)
    award = award_merge.drop_duplicates(award_cols)
    award = award[award_cols]
    award['header.dockeyverkey'] = (award['header.dockey'].map(str)
        + award['header.verkey'].map(str))
    return award

def join_awards_financial(awards, financial):
    """merge financial and awards records"""

    # aggregate financial data by tas, object class, program activity
    tas_agg = financial[[
        'tas','gl_code_combinations.segment5',
            'gl_code_combinations.segment4',
        'outlay_amt', 'obligated_amt']].groupby(
            ['tas', 'gl_code_combinations.segment5',
                'gl_code_combinations.segment4']
            ).sum()
    # add data act detailed data from financial system
    tas_agg.reset_index(inplace = True)
    # pull in some TAS-level info to simulate those numbers
    # (pulled these from the budget appendix as a stand-in)
    tas = pd.read_csv(
        'data/other/sba_tas_fy2014_summary.csv',
        usecols = ['tas', 'acct_ba_appropriated',
            'acct_other_budgetary_resources',
            'acct_total_budgetary_resources'],
            thousands = ',',
            dtype = {'acct_ba_appropriated' : np.int64,
                'acct_other_budgetary_resources' : np.int64,
                'acct_total_budgetary_resources' : np.int64}
    )
    tas['tas'] = tas['tas'].str[1:3] + tas['tas'].str[4:8]
    tas_agg = pd.merge(
        tas_agg,
        tas
    )
    everything = pd.merge(
        tas_agg,
        financial[['tas', 'gl_code_combinations.segment5',
            'gl_code_combinations.segment4', 'po_headers_all.segment1',
            'po_lines_all.item_description',
            'po_distributions_all.attribute10',
            'po_distributions_all.attribute11',
            'gl_code_combinations.segment3']],
        left_on = ['tas','gl_code_combinations.segment5',
            'gl_code_combinations.segment4'],
        right_on = ['tas','gl_code_combinations.segment5',
            'gl_code_combinations.segment4']
    )
    everything = everything.rename(
        columns = {'po_headers_all.segment1' : 'award_num'})
    # add data act detailed data from awards system
    awards = awards[['header.docnum',
        'header.versionnum',
        'header.amount', #total award amount
        'itemacct.obligatedamt',
        'header.awardtype',
        'grantheader.sba1222countyname',
        'grantheader.sba1222countycode',
        'grantheader.recipientcountrycode',
        'grantheader.recipientcountryname',
        'grantheader.sba1222congdistno',
        'docvendor.name',
        'docvendor.duns',
        'docvendor.address1',
        'docvendor.address2',
        'docvendor.address3',
        'docvendor.city',
        'docvendor.state',
        'docvendor.zip',
        'docaddr.name',
        'faadsciv.recordtype',
        'faadsciv.assistancetranstype',
        'faadsciv.countycityname',
        'faadsciv.countycitycode',
        'faadsciv.principalstatecode',
        'faadsciv.principalstatename',
        'faadsciv.placeofperfzip',
        'faadsciv.placeofperfcountrycode',
        'faadsciv.placeofperfcountryname',
        'faadsciv.cfdaprogramnumber',
        'faadsciv.cfdaprogramtitle',
        'faadsciv.recipienttype',
        'funding_agency_name',
        'funding_agency_code',
        'funding_sub_tier_agency_name',
        'funding_sub_tier_agency_code',
        'awarding_agency_name',
        'awarding_agency_code',
        'awarding_sub_tier_agency_name',
        'awarding_sub_tier_agency_code',
        'itemacct.itemacctkey'
    ]]
    awards = awards.rename(columns = {'header.docnum' : 'award_num'})
    everything = pd.merge(
        everything,
        awards,
        left_on = 'award_num',
        right_on = 'award_num'
    )

    everything = everything.rename(columns = {
        'gl_code_combinations.segment5' : 'object_class',
        'gl_code_combinations.segment4' : 'program_activity_code',
        'outlay_amt' : 'acct_outlay_amt',
        'obligated_amt': 'acct_obligated_amt',
        'po_lines_all.item_description' : 'award_desc',
        'po_distributions_all.attribute10' : 'period_of_perf_start_date',
        'po_distributions_all.attribute11' : 'period_of_perf_end_date',
        'gl_gl_code_combinations.segment3': 'funding_office',
        'header.versionnum' : 'award_mod',
        'header.amount' : 'award_potential_value',
        'itemacct.obligatedamt' : 'funding_action_obligation',
        'header.awardtype' : 'award_type',
        'grantheader.sba1222countyname' : 'recipient_county_name',
        'grantheader.sba1222countycode' : 'recipient_county_code',
        'grantheader.sba1222congdistno' : 'pop_cong_district',
        'docaddr.name' : 'awarding_office_name',
        'docvendor.name' : 'recipient_name',
        'docvendor.duns' : 'duns',
        'docvendor.address1' : 'recipient_addr1',
        'docvendor.address2' : 'recipient_addr2',
        'docvendor.address3' : 'recipient_addr3',
        'docvendor.city' : 'recipient_city',
        'docvendor.state' : 'recipient_state',
        'docvendor.zip' : 'recipient_zip',
        'faadsciv.recordtype' : 'record_type',
        'faadsciv.assistancetranstype' : 'type_of_transaction',
        'faadsciv.countycityname' : 'pop_city_name',
        'faadsciv.countycitycode' : 'pop_city_code',
        'faadsciv.principalstatecode' : 'pop_state_code',
        'faadsciv.principalstatename' : 'pop_state_name',
        'faadsciv.placeofperfzip' : 'pop_zip',
        'faadsciv.cfdaprogramnumber' : 'cfda_num',
        'faadsciv.cfdaprogramtitle' : 'cfda_desc',
        'faadsciv.recipienttype' : 'recipient_type',
        'grantheader.recipientcountrycode': 'recipient_country_code',
        'grantheader.recipientcountryname' : 'recipient_country_name'
    })
    return everything

def run():

    parser = argparse.ArgumentParser(description="Read exports from SBA financial and award systems and write out combined file in DATA Act format")
    parser.add_argument('-o', dest='outfile', help='the .csv file that contains the combined data')

    args = parser.parse_args()
    outfile = args.outfile

    awards = prep_awards()
    print ('\nProcessed {} awards/mods/award line items from Prism'.format(
        len(awards.index)))
    awards.to_csv('data/data_act_award_details.csv', index = False)
    financial = prep_financial()
    print ('\nProcessed {} purchase orders/distributions from JAAMS'.format(
        len(financial.index)))
    financial.to_csv('data/data_act_financial_details.csv', index = False)
    data_act = join_awards_financial(awards, financial)
    if not outfile:
        outfile = 'data/data_act.csv'
    data_act.to_csv('{}'.format(outfile), index = False)
    print('DATA Act combined file ({} records) written to {}'.format(
        len(data_act.index), outfile))
    return data_act

data_act = run()
