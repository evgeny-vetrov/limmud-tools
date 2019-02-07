import urllib
import requests
import sys
import json
from os import listdir
from os.path import isfile, join

token = open('token.txt').read()
store_id = 16157264




option_files = [join('options',f) for f in listdir('options') if isfile(join('options', f))]
for option_file in option_files:
    option_json = json.loads(open(option_file).read())
    product_ids = option_json['product_ids']
    data = option_json['data']
    data = {
            "options" : data
           }
    for product_id in product_ids:
        # todo send for each order options
        request_url = 'https://app.ecwid.com/api/v3/{store_id}/products/{id}?token={token}'.format(store_id=store_id, token=token, id=product_id)
        #request_url = 'https://app.ecwid.com/api/v3/{store_id}/products/{id}'.format(store_id=store_id, id=product_id)
        print(request_url)
        resp = requests.put(request_url, json=data)
        print(resp.text)
        print('product_id:{} respose:{}'.format(product_id, resp.status_code))
