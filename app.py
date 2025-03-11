from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity
import os
import asyncio

# Initialize Flask app
app = Flask(__name__)

# Bot settings
settings = BotFrameworkAdapterSettings(
    app_id=os.getenv("MICROSOFT_APP_ID"), 
    app_password=os.getenv("MICROSOFT_APP_PASSWORD")
)
adapter = BotFrameworkAdapter(settings)

# Function to handle incoming messages
async def turn_logic(turn_context: TurnContext):
    await turn_context.send_activity("Hello! I am Trinite Chatbot. How can I assist you?")

# API route for bot messages
@app.route("/api/messages", methods=["POST"])
def messages():
    body = request.json
    activity = Activity().deserialize(body)

    # Run async function in event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(adapter.process_activity(activity, "", turn_logic))

# Run Flask app (for local testing)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
