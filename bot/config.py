import os
from dotenv import load_dotenv

load_dotenv()

class DefaultConfig:
    PORT = 3978
    APP_ID = os.getenv("MICROSOFT_APP_ID", "")
    APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "")
    LUIS_APP_ID = os.getenv("LUIS_APP_ID", "")
    LUIS_API_KEY = os.getenv("LUIS_API_KEY", "")
    LUIS_API_HOST_NAME = os.getenv("LUIS_API_HOST_NAME", "luis-ai.cognitiveservices.azure.com/")
