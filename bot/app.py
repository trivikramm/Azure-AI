from aiohttp import web
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, ConversationState, MemoryStorage, ActivityHandler, TurnContext
from botbuilder.ai.luis import LuisApplication, LuisRecognizer
from config import DefaultConfig
from botbuilder.schema import Activity

CONFIG = DefaultConfig()
SETTINGS = BotFrameworkAdapterSettings("", "")
ADAPTER = BotFrameworkAdapter(SETTINGS)
MEMORY = MemoryStorage()
CONVERSATION_STATE = ConversationState(MEMORY)

LUIS_APP = LuisApplication(
    CONFIG.LUIS_APP_ID,
    CONFIG.LUIS_API_KEY,
    f"https://{CONFIG.LUIS_API_HOST_NAME}"
)
LUIS_RECOGNIZER = LuisRecognizer(LUIS_APP)

class CustomerServiceBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        luis_result = await LUIS_RECOGNIZER.recognize(turn_context)
        intent = luis_result.get_top_scoring_intent()

        if intent.intent == "Greeting":
            await turn_context.send_activity("Hello! How can I help you today?")
        elif intent.intent == "Help":
            await turn_context.send_activity("I can help you with product information, orders, and support.")
        elif intent.intent == "OrderStatus":
            await turn_context.send_activity("Please provide your order number for status.")
        else:
            await turn_context.send_activity("I'm not sure I understand. Could you rephrase that?")

BOT = CustomerServiceBot()

async def messages(req: web.Request) -> web.Response:
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return web.Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return web.json_response(data=response.body, status=response.status)
    return web.Response(status=201)

APP = web.Application()
APP.router.add_post("/api/messages", messages)

if __name__ == "__main__":
    try:
        print("\nBot server starting...")
        print(f"Listening on http://localhost:{CONFIG.PORT}/api/messages")
        web.run_app(APP, host="localhost", port=CONFIG.PORT)
    except Exception as error:
        raise error