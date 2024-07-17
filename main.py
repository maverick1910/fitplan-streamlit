import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as lang_router

# Routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(lang_router, prefix="/llm-openai", tags=["OpenAI model"])


@app.get("/")
async def read_root():
    return {"Message : ": "Success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000,
                log_level="info", reload=True)
