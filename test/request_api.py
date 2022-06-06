#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:01:11 2022

@author: Ivan Nemov
"""


import requests
import json

# prepare
base_url = 'http://127.0.0.1'
port = '8000'
route = '/square'
final_url = (':'.join([base_url, port]) if port != '' else base_url) + route
payload = json.dumps({'val': 3.56})

# get response on request
response = requests.post(final_url, json = payload, timeout = 2)
res = json.loads(response.text)
response.close()

# show results
print('Result: ')
print(res['res'])
print('\n')

print('Response code and reason: ')
print(response.status_code, response.reason)