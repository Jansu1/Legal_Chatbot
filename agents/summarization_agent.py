import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from agents.base_agent import BaseAgent

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class SummarizationAgent(BaseAgent):
    def __init__(self, api_key):
        super().__init__("SummarizationAgent")
        self.llm = ChatGroq(model="llama3-8b-8192", api_key=api_key)

    def process(self, text):
        print("The text is ",text)
        response = self.llm.invoke([
            SystemMessage(content="Summarize this legal text:"),
            HumanMessage(content=str(text))
        ])
        return response.content


