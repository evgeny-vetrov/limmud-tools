import sys
import urllib as u
import pprint
import json

request = sys.argv[1]
token = open('token.txt').read()
store_id = '16157264'
url = 'https://app.ecwid.com/api/v3/{}/'.format(store_id) + request
if '?' in url:
    url = url + '&token={}'.format(token)   
else:
    url = url + '?token={}'.format(token)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.loads(u.urlopen(url).read()))
#print(u.urlopen(url).read())

