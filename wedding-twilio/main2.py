# Download the helper library from https://www.twilio.com/docs/python/install
import requests
from twilio.rest import Client
import pandas as pd

body = """
חברות וחברים,
שמחים ומתרגשים לראותכם מחר בשמחתנו.

משפחות דביר וליברמן
"""

account_sid = 'AC66544bf58e6df87e45af411fe7c65bee'
auth_token = '4e9a47da561f4f5be7d70bc6fa48db42'

df = pd.read_csv('./confirmations.csv')

name = df['name']
phone = df['phone']
people = df['כמה מגיעים?']
answer = df['ענה להודעה?']

all_columns = zip(name, phone, people, answer)

data = []

for line in all_columns:
    name, phone, people, answer = line

    if not isinstance(name, str):
        print('ERROROROROROROR: ', name)
        continue

    if isinstance(phone, str) or (phone, int):
        phone = str(phone)
        # Fix phones
        if phone.startswith('5'):
            phone = '+972' + phone
        elif phone.startswith('0'):
            # phone = phone.replace('0', '+972')
            phone = '+972' + phone[1:]

        # Fix name
        name = name.strip()

        data.append({'name': name, 'phone': phone, 'people': str(people), 'answer': answer})

for d in data:
    print('d', d)
    if d['phone'] == 'nan' or d['people'] == 'nan' or d['answer'] == 'nan':
        print('skipped')
        continue

    if not(int(d['people']) > 0 and d['answer'] == 'כ'):
        print('skipped')
        continue

    d['message'] = body

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=d['message'],
             from_='+19785232688',
             to=d['phone']
         )

    print("sid is: ", message.sid, 'phone', phone)
