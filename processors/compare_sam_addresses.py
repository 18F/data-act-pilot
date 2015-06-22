import csv
import time
import usaddress
from processors.get_sam_data import SamData


def get_address(record):
    results = {}
    results['address1'] = record['docvendor.address1']
    results['address2'] = record['docvendor.address2']
    results['address3'] = record['docvendor.address3']
    results['city'] = record['docvendor.city']
    results['name'] = record['docvendor.name']
    results['state'] = record['docvendor.state']
    results['zip'] = record['docvendor.zip']
    return results


def format_sam_address(address):
    result = ' '.join(filter(None, [address.get('Line1'),
                                    address.get('Line2'),
                                    address.get('City'),
                                    address.get('stateorProvince'),
                                    '-'.join(filter(None,
                                                    [address.get('Zip'),
                                                     address.get('Zip4')]))
                                    ]))
    return result.lower()


def format_sba_address(address):
    result = ' '.join(filter(None, [address.get('address1'),
                                    address.get('address2'),
                                    address.get('address3'),
                                    address.get('city'),
                                    address.get('state'),
                                    address.get('zip')]))
    return result.lower()


def compare_addresses(address1, address2):
    try:
        a1 = usaddress.tag(address1)
        a2 = usaddress.tag(address2)
        shared = dict(set(a1[0].items()) & set(a2[0].items()))
        return shared
    except RepeatedLabelError:
        pass


def check_match(shared):
    fields = ['AddressNumber',
              'StreetName',
              'PlaceName',
              'StateName']
    if set(fields).issubset(shared.keys()):
        return True
    return False


def run():
    f = csv.DictReader(open('data/data_act_test.csv'))
    r = {row['docvendor.duns']: {'sba': get_address(row)} for row in f}
    for duns in r.keys():
        print "Fetching data for {} from SAM Api".format(duns)
        time.sleep(2)
        data = SamData(duns)
        mailing = data.get_field('mailingAddress')
        sam_address = data.get_field('samAddress')
        r[duns]['mailing'] = mailing
        r[duns]['sam'] = sam_address
    address_strings = {k: {'sam': format_sam_address(r[k]['sam']),
                           'sba': format_sba_address(r[k]['sba']),
                           'mailing': format_sam_address(r[k]['mailing'])}
                       for k in r.keys()}
    results = {}
    for duns in address_strings:
        mail = compare_addresses(address_strings[duns]['sba'],
                                 address_strings[duns]['mailing'])
        sam = compare_addresses(address_strings[duns]['sba'],
                                address_strings[duns]['sam'])
        results[duns] = {}
        if mail:
            results[duns]['mail'] = {'match': mail,
                                     'pass': str(check_match(mail))}
        else:
            results[duns]['mail'] = 'Can\'t parse address for {}'.format(duns)
        if sam:
            results[duns]['sam'] = {'match': sam,
                                    'pass': str(check_match(sam))}
        else:
            results[duns]['sam'] = 'Can\'t parse address for {}'.format(duns)
    print results

run()
