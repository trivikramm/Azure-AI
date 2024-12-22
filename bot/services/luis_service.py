from botbuilder.ai.luis import LuisApplication, LuisRecognizer, LuisPredictionOptions

class LuisService:
    def __init__(self, app_id, api_key, api_host_name):
        luis_application = LuisApplication(app_id, api_key, f"https://{api_host_name}")
        self.recognizer = LuisRecognizer(luis_application)

    async def recognize(self, context):
        return await self.recognizer.recognize(context)