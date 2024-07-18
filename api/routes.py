from fastapi import APIRouter
from llm_models.gemini import GeminiModel
from llm_models.anthropic import AnthropicModel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from templates.generate_plan import fetch_template_data
from models.user_model import UserInput
from models.plan_model import MealWorkoutPlan

router = APIRouter()
gemini_llm = GeminiModel.gemini_init()
claude_llm = AnthropicModel.anthropic_init()

parser = PydanticOutputParser(pydantic_object=MealWorkoutPlan)


@router.post("/generate-plan")
def get_message(user_input: UserInput):
    try:
        template_content = fetch_template_data(user_input.dict())
        full_template = f"{template_content}\n\n{{format_instructions}}"

        prompt = PromptTemplate(
            template=full_template,
            input_variables=[],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | gemini_llm | parser

        result = chain.invoke({})
        return {
            'status': "200",
            'data': result
        }
    except Exception as e:
        import logging
        logging.error(str(e), exc_info=True)
        return {
            'status': "500",
            'data': str(e)
        }
