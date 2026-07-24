AquaGuard AI
💧 Project Overview

AquaGuard AI is an autonomous AI agent that monitors household water purifier telemetry in real time. It continuously checks water quality (TDS) and filter health, automatically alerts users when unsafe conditions are detected, and places replacement filter orders when the filter reaches a critical level.

This project supports United Nations Sustainable Development Goal (SDG 6 – Clean Water and Sanitation).

Problem Statement

Most households replace water purifier filters after a fixed period instead of checking the actual condition.

This can result in:

Unsafe drinking water
High TDS levels
Worn-out filters
No real-time alerts
Delayed maintenance
Solution

AquaGuard AI continuously monitors:

Water TDS
Filter Life

The AI agent automatically:

Detects unsafe water
Sends WhatsApp alerts
Orders replacement filters
Displays the analysis on a dashboard
Features

✅ Real-time telemetry monitoring

✅ AI-powered decision making using Gemini

✅ WhatsApp alert notifications using Twilio

✅ Automatic replacement filter ordering

✅ Interactive Streamlit Dashboard

✅ Sensor simulator for testing

Tech Stack
Programming Language
Python 3.12
AI Framework
LangChain
LangGraph
LLM
Google Gemini API
Frontend
Streamlit
Notifications
Twilio WhatsApp API
Environment Variables
python-dotenv
Project Structure
AquaGuard-AI/
│
├── app.py
├── aquaguard_agent.py
├── sensor_simulator.py
├── tools.py
├── check_api.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
└── venv/
Workflow
Step 1

Sensor data is generated.

Example:

TDS = 620
Filter = 80%

↓

Step 2

The AI Agent receives telemetry.

↓

Step 3

Gemini analyzes the data.

↓

Step 4

If TDS > 500

↓

WhatsApp Alert Sent

↓

Step 5

If Filter Life ≤ 5%

↓

Replacement Filter Ordered

↓

WhatsApp Notification Sent

↓

Step 6

Dashboard displays the final AI decision.

AI Rules

Safe Water

TDS ≤ 300 ppm

Unsafe Water

TDS > 500 ppm

Critical Filter

Filter Life ≤ 5%
Installation

Clone the repository

git clone YOUR_GITHUB_LINK

Go inside the folder

cd AquaGuard-AI

Create virtual environment

python -m venv venv

Activate

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
Environment Variables

Create a .env file

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

TWILIO_ACCOUNT_SID=YOUR_SID

TWILIO_AUTH_TOKEN=YOUR_AUTH_TOKEN

TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
Running the Project

Run Streamlit Dashboard

streamlit run app.py

Run Sensor Simulator

python sensor_simulator.py

Run Agent Directly

python aquaguard_agent.py
Example Output

Safe Water

Customer ID : CUST101

TDS : 120 ppm

Filter : 80%

Status : Normal

Unsafe Water

TDS : 620 ppm

WhatsApp Alert Sent

Critical Filter

Filter Life : 3%

Replacement Ordered

WhatsApp Alert Sent
Screenshots

Add screenshots like:

Dashboard
Safe Water Output
Unsafe Water Output
WhatsApp Alert
Terminal Output
Filter Replacement Output

Example:

screenshots/

dashboard.png

safe_output.png

unsafe_output.png

whatsapp_alert.png
Future Improvements
IoT Sensor Integration
Live Database
User Login
Cloud Deployment
Email Notifications
Analytics Dashboard
Water Usage History
Multiple Customer Support
SDG Goal

SDG 6

Clean Water and Sanitation

AquaGuard AI helps households receive clean and safe drinking water through continuous AI monitoring.