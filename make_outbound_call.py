import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)
call = client.calls.create(to="+18507740771", 
                       from_="+12054330359", 
                       url="http://demo.twilio.com/docs/voice.xml")