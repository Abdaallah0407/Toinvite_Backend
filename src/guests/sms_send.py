# Download the helper library from https://www.twilio.com/docs/python/install
import hashlib
import os
import uuid

import requests
from dicttoxml import dicttoxml
from twilio.rest import Client
from toinvite_core import settings

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
from toinvite_core.settings import NIKITA_USERNAME, NIKITA_SENDER, NIKITA_TEST, NIKITA_PASS, NIKITA_URL

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
from_phone = settings.TWILIO_NUMBER
client = Client(account_sid, auth_token)


def sms_send(to_phone, text):
    message = client.messages \
        .create(
            body=text,
            from_='+19592511918',
            to=to_phone
         )
    print(message.sid)


def nikita_sms_send(text, transformed_number):
    id_string = str(uuid.uuid4())
    data = {
        'login': NIKITA_USERNAME,
        'pwd': NIKITA_PASS,
        'id': hashlib.md5(id_string.encode()).hexdigest()[:12],
        'sender': NIKITA_SENDER,
        'text': text,
        'phones': [f'{transformed_number}'],
        'test': NIKITA_TEST
    }
    page = dicttoxml(data, custom_root='message', item_func=lambda x: x[:-1], attr_type=False)
    answer = requests.post(NIKITA_URL, data=page, headers={'Content-Type': 'application/xml'})