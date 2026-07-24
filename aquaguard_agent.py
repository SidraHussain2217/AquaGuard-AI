import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import send_alert_notification, order_filter_replacement

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

tools = [
    send_alert_notification,
    order_filter_replacement
]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are AquaGuard AI.

You MUST use the available tools.

Rules:

1. Safe TDS <= 300 ppm
2. Unsafe TDS > 500 ppm
3. Filter critical if life <= 5%

If TDS > 500:
- Call send_alert_notification
- message = "WARNING: High TDS level detected (XXX ppm). Please avoid drinking this water."
- phone_number = customer's phone

If filter life <= 5:
- Call order_filter_replacement
- Call send_alert_notification

Never just describe the action.
Always call the tool whenever the condition is met.
"""
)


def run_telemetry(tds, filter_life, customer_id, phone):

    telemetry = f"""
Customer ID: {customer_id}
Phone: {phone}

Current TDS: {tds}
Filter Life: {filter_life}%
"""

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": telemetry
                }
            ]
        }
    )

    # Get AI response
    ai_response = response["messages"][-1].content

    # If LangChain returns a list, extract only the text
    if isinstance(ai_response, list):
        ai_response = ai_response[0]["text"]

    print("\n====== AI RESPONSE ======")
    print(ai_response)

    return ai_response


if __name__ == "__main__":

    run_telemetry(
        tds=600,
        filter_life=80,
        customer_id="CUST101",
        phone="whatsapp:+919811922549"
    )