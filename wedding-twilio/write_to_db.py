# Download the helper library from https://www.twilio.com/docs/python/install
import os

import requests
import pandas as pd

df = pd.read_csv('./invitees.csv')

name = df['name']
phone = df['phone']
people = df['כמה מגיעים?']
answer = df['ענה להודעה']

all_columns = zip(name, phone, people, answer)

data = []

for line in all_columns:
    name, phone, group = line
    if isinstance(phone, str):

        # Fix phones
        if phone.startswith('5'):
            phone = '+972' + phone
        elif phone.startswith('0'):
            phone = phone.replace('0', '+972')

        # Fix name
        name = name.strip()

        data.append({'name': name, 'phone': phone, 'group': group})

# # 142.93.161.46
for d in data:
    resp = requests.post('http://localhost:3001/api/attendies', json=d)
    __id = resp.text
    d['id'] = __id

