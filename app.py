from flask import Flask, request, jsonify
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from botbuilder.schema import Activity
import os

app = Flask(__name__)

# Bot settings
settings = BotFrameworkAdapterSettings(app_id=os.getenv("MICROSOFT_APP_ID"), app_password=os.getenv("MICROSOFT_APP_PASSWORD"))
adapter = BotFrameworkAdapter(settings)

# Handle messages from Azure Bot Service
@app.route("/api/messages", methods=["POST"])
def messages():
    body = request.json
    activity = Activity().deserialize(body)
    
    async def turn_logic(turn_context):
        await turn_context.send_activity("Hello! I am Trinite Chatbot. How can I assist you?")
    
    return adapter.process_activity(activity, "", turn_logic)

if __name__ == "__main__":
    app.run(port=3978)
