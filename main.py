# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

phone_num = '+19785232688'
account_sid = 'AC66544bf58e6df87e45af411fe7c65bee'
auth_token = '4e9a47da561f4f5be7d70bc6fa48db42'

test_dest = '+972547422149'

MESSAGE = """
הנכם מוזמנים לחתונה של עומר ועינב
אנא השיבו את מספר האנשים שאתם מתכוונים להגיע!
"""

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=MESSAGE,
         from_=phone_num,
         to=test_dest
     )

print(message.sid)
