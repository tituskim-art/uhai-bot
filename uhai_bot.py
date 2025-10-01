from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "challenge" in incoming_msg:
        msg.body("🌱 Life Skill: Practice gratitude today—thank someone sincerely.")
    elif "story" in incoming_msg:
        msg.body("🕊️ Story: A boy forgives his brother after a fight. What does forgiveness free us from?")
    else:
        msg.body("👋 Welcome to Uhai! Reply with 'challenge' or 'story' to begin.")

    return str(resp)