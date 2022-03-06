from optparse import Values
from twilio.rest import Client
from dotenv import dotenv_values

class WhatsappHandler:
    values = dotenv_values()
    sid = values["TWILIO_ACCOUNT_SID"]
    token = values["TWILIO_AUTH_TOKEN"]
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    def __init__(self):
        self.client = Client(self.sid,self.token)
        self.from_whatsapp_number= self.values["FROM_TEL_NR"]
        self.to_whatsapp_number= self.values["TO_TEL_NR"]


    def send_message(self, data):
        self.client.messages.create(body=data,
                            from_=self.from_whatsapp_number,
                            to=self.to_whatsapp_number)