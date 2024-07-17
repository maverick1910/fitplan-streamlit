import os
from dotenv import load_dotenv

load_dotenv()


LANGCHAIN_API_KEY = os.environ.get('LANGCHAIN_API_KEY')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
