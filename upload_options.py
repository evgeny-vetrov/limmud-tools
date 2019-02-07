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
    templates = option_json['templates']
    for group in option_json['groups']:
        product_ids = group['product_ids']
        template_ids = data['template_ids']
        data = []
        for tid in template_ids:
            data.extend(templates[tid])
        for product_id in product_ids:
            request_url = 'https://app.ecwid.com/api/v3/{store_id}/products/{id}?token={token}'.format(store_id=store_id, token=token, id=product_id)
            resp = requests.put(request_url, json=data)
            print('product_id:{} respose:{}'.format(product_id, resp.status_code))

