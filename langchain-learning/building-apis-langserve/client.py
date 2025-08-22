#create a streamlit  chat interface
import streamlit as st 
import requests

#definnig the functions to be used - inmvoke has to  be added to invoke the langserve and this is a norm
def getOllama_response(input_text):
    response = requests.post("http://localhost:3000/ollama/essay/invoke", json={"input": {"topic": input_text}})
    return response.json()['output']['content']



#streamlit ui using the function 
st.title("chat frontend interface")
input_text = st.text_input("enter the topic you want to have an essay on")

if input_text:
    response= getOllama_response(input_text)
    st.write(response)