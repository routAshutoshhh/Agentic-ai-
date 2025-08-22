from fastapi import FastAPI
from langserve  import add_routes
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
#from langchain.chat_models import ChatOpenAI   #will only use to understand thsi usage and nnot having any api keys for this
import uvicorn
import os

#STEP1 - LOADING KEYS AS VARIABLES USING CONFIG FILE
from config import  OLLAMA_API_KEY
# from dotenv import load_dotenv


# #loading the dotenv
# load_dotenv()

# #using the open ai key - actually we dont need to do this  as the load_dotenv() will take care for this
# #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# # instead just do this
# openAI_api_key = os.getenv("OPENAI_API_KEY")#since we dont have any such thing here 


#STEP2 - CREATING A FASTAPI APPLICATION
app = FastAPI(
    title="LangChain API",
    description="API  server for interacting with LangChain",
    version="0.1.0"
)


#STEP3 - DEFINING THE MODELS with the langchain 
MODEL_OLLAMA = OllamaLLM(model="phi:latest")
#MODEL_OPENAI = ChatOpenAI() # since its empty then there will be showing error


#STEP4 - DEFINING THE PROMPT TEMPLATE
prompt_ollama = ChatPromptTemplate.from_template("Please write an essay on {topic}.")
# prompt_openai=ChatPromptTemplate.from_messages("please write an essay on {topic}")


#STEP5 - we need to create the chains for the models 
chain_Ollama = prompt_ollama|MODEL_OLLAMA
#chain_OpenAI = prompt_openai|MODEL_OPENAI


#STEP-optional - creating raw endpoints by passing models in the langserve
add_routes(app,MODEL_OLLAMA,path="/ollama/raw")
#add_routes(app,MODEL_OPENAI,path="/openai/essayO/raw")

#STEP6 - DEFINING THE API ENDPOINTS WITH THE LANGSERVE
#for Ollama
add_routes(app,chain_Ollama,path="/ollama/essay")

#for OpenAI
#add_routes(app,chain_OpenAI,path="/openai/essayO")- not required - 


##ust run -  uvicorn main:app --reload --host 127.0.0.1 --port 3000