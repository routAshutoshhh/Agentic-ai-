# from langchain_ollama import ChatOllama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as stl
import os
from dotenv import load_dotenv

#initialising the load_dotenv()
load_dotenv()

#after this we need to make the environment variable call
##os.environ["OLLAMA_API_KEY"] = os.getenv("OLLAMA_API_KEY") or ""
#for langchain a tracking key calling 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") or ""
#we would need to call one specific environment variable
os.environ["LANGCHAIN_TRACING_V2"]  =  "true"

##creating chatbot after this\

 #to create the chatbot we first need to create the prompt for doing that we need to do it by chatbot template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant who does not talk disrespectfully to anyone always treat the user as the king/boss, please provide resppnse to the queriess of the user in the most nicest wway possible , always calling the user `sir`"),
        ("user","Question: {question}")
    ]
 )


# """
# so the logic is the chatprompt tempplate does the tempalating for the model and the ther repsonse come from the ollama or chatgpt
# then the strOutputParser is used to parse the output from the model and extract the relevant information
# """

##creating streamlit for the chatui
stl.title("small ai chatbot")
input_text = stl.text_input("please ask anything that you would like")


#now we need to call the llama llm
llm = OllamaLLM(model="phi:latest")
output = StrOutputParser()


#building a chaino of execution 

chain = prompt|llm|output

#if we have the input text we can invoke the chain and on the stremlit 
if input_text:
    with stl.spinner("Thinking... 🤔"):
        response = chain.invoke({"question": input_text})
        stl.write("DEBUG:", response)  # 👈 check if response is empty
    stl.success(response if response else "⚠️ No response from model")




