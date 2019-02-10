import requests
import json
from copy import deepcopy
from collections import defaultdict
from os import listdir
from os.path import isfile, join

token = open('token.txt').read()
store_id = 16157264


def process_templates(templates):
    """
    builds templates since they can contain references to other templates
    :type templates: dict
    """
    keys = set(templates.keys())
    cache = {}
    for key in keys:
        templates[key] = process_template(templates, key, cache)


def process_template(templates, template_id, processed):
    if template_id in processed:
        return deepcopy(processed[template_id])
    res = []
    template = templates[template_id]
    for val in template:
        if isinstance(val, basestring):
            res.extend(process_template(templates, val, processed))
        else:
            res.append(deepcopy(val))
    processed[template_id] = res
    return deepcopy(res)


option_files = [join('options', f) for f in listdir('options') if isfile(join('options', f))]
for option_file in option_files:
    option_json = json.loads(open(option_file).read())
    templates = option_json['templates']
    process_templates(templates)
    for group in option_json['groups']:
        product_ids = group['product_ids']
        template_ids = group['template_ids']
        data = []
        for tid in template_ids:
            data.extend(deepcopy(templates[str(tid)]))
        options_count = defaultdict(int)
        for option in data:
            option_name = option['name']
            cnt = options_count[option_name]
            if cnt != 0:
                option['name'] = option_name + " (" + str(cnt) + ")"
            options_count[option_name] = cnt + 1
        data = {"options": data}
        for product_id in product_ids:
            # if product_id == 130555267:
            #     print(json.dumps(data))
            # else:
            #     continue
            request_url = 'https://app.ecwid.com/api/v3/{store_id}/products/{id}?token={token}'.format(
                store_id=store_id, token=token, id=product_id)
            resp = requests.put(request_url, json=data)
            print('product_id:{} response:{}'.format(product_id, resp.status_code))
