# Download the helper library from https://www.twilio.com/docs/python/install
import requests
from twilio.rest import Client
import pandas as pd

body = """
היי,
שמחים להזמינכם לחתונתם של עינב דביר ועומר ליברמן ב15.8.22.
לפרטים נוספים ואישור הגעה היכנסו לקישור הבא:
http://www.einav-omer.com/?id={id}

במידה והקישור לא נפתח בהצלחה, ניתן לאשר דרך הקישור הבא:
http://www.einav-omer.com/

או בהודעת וואטסאפ למספר 0547422149

נשמח לראותכם בין אורחינו
"""

df = pd.read_csv('./invitees.csv')

name = df['name']
phone = df['phone']
group = df['group']

all_columns = zip(name, phone, group)

data = []

for line in all_columns:
    name, phone, group = line
    if isinstance(phone, str) or (phone, int):
        phone = str(phone)
        # Fix phones
        if phone.startswith('5'):
            phone = '+972' + phone
        elif phone.startswith('0'):
            phone = phone.replace('0', '+972')

        # Fix name
        name = name.strip()

        data.append({'name': name, 'phone': phone, 'group': group})

# # 46.101.102.14
for d in data:
    resp = requests.post('http://46.101.102.14:3001/api/attendies', json=d)
    __id = resp.text
    d['id'] = __id
    d['message'] = body.format(id=__id).replace('"', '')


for d in data:
    print(f"Sending to {d['phone']} the message {d['message']}")

    account_sid = 'AC66544bf58e6df87e45af411fe7c65bee'
    auth_token = '4e9a47da561f4f5be7d70bc6fa48db42'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             # messaging_service_sid='MG9752274e9e519418a7406176694466fa',
             body=d['message'],
             from_='+19785232688',
             # from_='whatsapp:+14155238886',
             to=d['phone']
         )

    print("Sid is: ", message.sid)
