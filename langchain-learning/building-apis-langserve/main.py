from fastapi import FastAPI
from langserve  import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

import uvicorn
import os
from dotenv import load_dotenv


#loading the dotenv
load_dotenv()



##creating a fastapi  application 
app = FastAPI(
    title="LangChain API",
    description="API  server for interacting with LangChain",
    version="0.1.0"
)


##creating routes using langserve
add_routes(
    app,
    OllamaLLM(),
    path="/api/ollama"
)

#creating models 
#creating open ai llm model - that we are not going to use for the things
openai_llm =


#creating a  llama model 
llama_llm = OllamaLLM(model="phi:latest")

#creating prompt
prompt = ChatPromptTemplate.from_template("write me an essay for coding beneifts ")
