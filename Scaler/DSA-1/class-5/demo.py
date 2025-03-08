import sys
import csv
import requests
import json

sms_endpoint = sys.argv[sys.argv.index('--sms_endpoint') + 1]
token = "Bearer " + sys.argv[sys.argv.index('--token') + 1]
csv_path = sys.argv[sys.argv.index('--csv_path') + 1]

rest_api = sms_endpoint + '/esms/1.0/rest/_proxy'


def post_call_sm_api(url, params):
    try:
        r = requests.post(url, headers={
            "Accept": "application/json",
            "Authorization": token
        }, json=params)
        return r.json() if requests.codes.ok == r.status_code else None
    except Exception as e:
        print(e)
        return None


def put_call_sm_api(url, params):
    try:
        r = requests.put(url, headers={
            "Accept": "application/json",
            "Authorization": token
        }, json=params)
        return r.json() if requests.codes.ok == r.status_code else None
    except Exception as e:
        print(e)
        return None


def get_call_sm_api(url, params=None):
    if params is None:
        params = {}
    try:
        r = requests.get(url, headers={
            "Accept": "application/json",
            "Authorization": token
        }, params=params)
        return r.json() if requests.codes.ok == r.status_code else None
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    missing_index_arr = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            missing_index_arr.append(row)

    for missing_index in missing_index_arr:
        alias = missing_index['index']
        es_id = missing_index['es_id']
        business_name = missing_index.get('index').replace("_2025_3", "")

        try:
            add_alias_body = {
                "actions": [
                    {
                        "add": {
                            "index": business_name + '_v1_2025_2',
                            "alias": alias
                        }
                    }
                ]
            }

            request_body = {
                "esId": [es_id],
                "esIdType": "ASYNCSEARCH",
                "request": {
                    "method": "POST",
                    "path": "_aliases",
                    "parameters": {},
                    "body": json.dumps(add_alias_body)
                },
                "attributes": {
                    "businessName": "",
                    "confirmedURI": ""
                }
            }

            response = post_call_sm_api(rest_api, request_body)

            if response['success'] == 1:
                print('add alias success, alias={0}'.format(alias))
            else:
                print('add alias failed, alias={0}, error={1}'.format(alias, response))
        except Exception as e:
            print('add alias failed, alias={0}, error={1}'.format(alias, e))
