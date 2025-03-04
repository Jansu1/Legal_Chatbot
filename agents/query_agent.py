from backend.retrieval import Retrieval
from agents.base_agent import BaseAgent

class QueryAgent(BaseAgent):
    def __init__(self, vector_store):
        super().__init__("QueryAgent")
        self.retrieval = Retrieval(vector_store)  # Pass vector_store as an argument

    def process(self, query):
        print("The query is ",query)
        docs = self.retrieval.retrieve_documents(str(query))
        return [doc.page_content for doc in docs] if docs else ["No relevant legal information found."]
