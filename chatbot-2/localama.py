from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Search the topic u want")

# ollama LLAma2 LLm 
#llm=OllamaLLM(model="llama2")
# Set up the Groq model
model = ChatGroq(model="gemma2-9b-it", api_key=groq_api_key)
output_parser=StrOutputParser()
chain=prompt|model|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))