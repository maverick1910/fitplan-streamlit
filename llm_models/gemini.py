from config.env_config import GOOGLE_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiModel:
    @classmethod
    def gemini_init(cls):
        llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=GOOGLE_API_KEY)
        return llm
