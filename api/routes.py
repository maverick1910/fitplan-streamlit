from fastapi import APIRouter
from llm_models.gemini import GeminiModel
from llm_models.anthropic import AnthropicModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from templates.generate_plan import fetch_template_data
from models.user_model import UserInput

router = APIRouter()
gemini_llm = GeminiModel.gemini_init()
claude_llm = AnthropicModel.anthropic_init()

parser = StrOutputParser()


@router.post("/generate-plan")
def get_message(user_input: UserInput):
    try:
        template = fetch_template_data(user_input.dict())
        prompt = PromptTemplate.from_template(template)
        chain = prompt | gemini_llm | parser
        result = chain.invoke(user_input.dict())
        return {
            'status': "200",
            'data': result
        }
    except Exception as e:
        return {
            'status': "500",
            'data': str(e)
        }
