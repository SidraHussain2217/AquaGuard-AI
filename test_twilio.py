import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)

message = client.messages.create(
    body="✅ AquaGuard AI Test Message",
    from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
    to=os.getenv("MY_WHATSAPP_NUMBER")
)

print("Message SID:", message.sid)