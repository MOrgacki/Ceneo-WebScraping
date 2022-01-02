from twilio.rest import Client


class WhatsappHandler:
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    def __init__(self):
        self.client = Client()
        self.from_whatsapp_number='whatsapp:+14155238886'
        self.to_whatsapp_number='whatsapp:+48535964737'


    def send_message(self, data):
        self.client.messages.create(body=data,
                            from_=self.from_whatsapp_number,
                            to=self.to_whatsapp_number)