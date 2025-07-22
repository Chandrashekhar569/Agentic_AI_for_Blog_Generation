"""
=============================================
              Groq LLM File
=============================================
* This file handles integration with the Groq LLM via LangChain's `ChatGroq` interface.

* Key Responsibilities:
  - Loads environment variables using `python-dotenv`
  - Retrieves and authenticates the GROQ API key
  - Initializes the `ChatGroq` model for blog generation tasks

## Class: GroqLLM
* Encapsulates logic to set up and return the Groq-powered LLM object

## Function: get_llm()
* Configures the environment key and returns the Groq Chat model instance
* Contains placeholder logic for switching to OpenAI's GPT models if needed
_____________________________________________
"""

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
            load_dotenv()


    def get_llm(self):
          try:
            os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
            llm=ChatGroq(api_key=self.groq_api_key,model="meta-llama/llama-4-maverick-17b-128e-instruct")

            # For OpenAI
            # os.environ["OPENAI_API_KEY"]=self.openai_api_key=os.getenv("OPENAI_API_KEY")
            # llm = ChatOpenAI(api_key=self.open_api_key,model="gpt-4-turbo")

            print("LLM Running")

            return llm
          
          except Exception as e:
               raise ValueError("Error occurred with exception : {e}")
    
