# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from toinvite_core import settings

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = settings.TWILIO_ACCOUNT_SID 
auth_token = settings.TWILIO_AUTH_TOKEN
from_phone = settings.TWILIO_NUMBER
client = Client(account_sid, auth_token)


def sms_send(to_phone, text):
    message = client.messages \
        .create(
            body=text,
            from_=from_phone,
            to=to_phone
         )
    print(message.sid)
