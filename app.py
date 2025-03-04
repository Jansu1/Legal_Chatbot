import streamlit as st
from workflows.chatbot_graph import ChatbotGraph  # Absolute import
from dotenv import load_dotenv
import os

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.title("Legal Chatbot 🤖")

# Initialize chatbot (no need for build)
chatbot = ChatbotGraph(api_key=api_key)

user_query = st.text_input("Ask a legal question:")

if st.button("Submit"):
    response = chatbot.run(user_query)
    print("Chatbot response",response)
    st.write(response)
