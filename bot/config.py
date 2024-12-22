import os
from dotenv import load_dotenv

load_dotenv()

class DefaultConfig:
    PORT = 3978
    APP_ID = os.getenv("MICROSOFT_APP_ID", "5d11f002-b277-4231-a5df-61516f3a010a")
    APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "52b6f7ce-6aee-43ca-b583-a211c2da8c4d")
    LUIS_APP_ID = os.getenv("LUIS_APP_ID", "8bd16ad0-b10c-41bf-b8a0-5418b7ce2090")
    LUIS_API_KEY = os.getenv("LUIS_API_KEY", "9b333b87e2f24b57aec64c4ec78c1441")
    LUIS_API_HOST_NAME = os.getenv("LUIS_API_HOST_NAME", "luis-ai.cognitiveservices.azure.com/")