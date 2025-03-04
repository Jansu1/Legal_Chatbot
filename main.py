from workflows.chatbot_graph import ChatbotGraph
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if __name__ == "__main__":
    chatbot = ChatbotGraph(api_key=GROQ_API_KEY)  # Pass the API key

    while True:
        query = input("Ask a legal question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        response = chatbot.run(query)
        print("Chatbot Response:", response)
