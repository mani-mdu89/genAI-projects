from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
groq_api_key
model = ChatGroq(model="Gemma2-9b-It",api_key=groq_api_key)

from langserve import add_routes

system_template = "Translate the following into this particular language."
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])
parser = StrOutputParser()
chain = chat_prompt | model | parser

## Fast API
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain runnable interfaces."
)
add_routes(app, chain, path="/chain")

#Set up the entry point for the application and run it using Uvicorn.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)