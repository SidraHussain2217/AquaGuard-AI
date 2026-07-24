import os
from dotenv import load_dotenv
from twilio.rest import Client
from langchain_core.tools import tool

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN")
)
last_message = None

@tool
def send_alert_notification(message: str, phone_number: str) -> str:
    
    """
    Sends a WhatsApp alert to the user.
    """

    msg = client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_WHATSAPP_NUMBER"),
        to=phone_number
    )

    print("WhatsApp Message SID:", msg.sid)

    return f"WhatsApp alert sent successfully. SID: {msg.sid}"


@tool
def order_filter_replacement(customer_id: str) -> str:
    """
    Places a replacement filter order for the customer.
    """

    print("\n======= FILTER ORDER =======")
    print(f"Customer ID : {customer_id}")
    print("Replacement filter ordered.")
    print("============================\n")

    return f"Replacement filter ordered for {customer_id}."