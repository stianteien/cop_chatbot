import time
import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain_community.chat_models import ChatOpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


from langchain.memory import ConversationBufferMemory



class chatbot:
    def __init__(self):

        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
        os.environ["OPENAI_API_TYPE"] = st.secrets["OPENAI_API_TYPE"]
        os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]
        os.environ["OPENAI_ENGINE_NAME"] = st.secrets["OPENAI_ENGINE_NAME"]
        
        
        

        self.llm_chain = self.get_chain()


    @st.cache_resource
    def get_chain(_self):

        llm = ChatOpenAI(temperature=0.1, 
                               engine = os.environ.get("OPENAI_ENGINE_NAME"))
        
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content="Your are a cat. Only answer like a cat."
                ),  # The persistent system prompt
                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  # Where the memory will be stored.
                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  # Where the human input will injected
            ]
        )

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory,
        )

        return llm_chain



    def response(_self, prompt):
        
        response = _self.llm_chain.predict(human_input=prompt)

        return response


    def response_generator(_self, prompt):
        reponse = _self.response(prompt)

        for word in reponse.split():
            yield word + " "
            time.sleep(0.05)