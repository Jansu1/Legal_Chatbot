from langgraph.graph import StateGraph
from langgraph.graph.message import AnyMessage  # Use AnyMessage instead
from agents.query_agent import QueryAgent
from agents.summarization_agent import SummarizationAgent
from backend.vector_store import VectorStore
from workflows.state import LegalQueryState

class ChatbotGraph:
    def __init__(self, api_key):
        self.vector_store = VectorStore()
        self.query_agent = QueryAgent(self.vector_store)
        self.summarization_agent = SummarizationAgent(api_key)

        self.graph = StateGraph(LegalQueryState)
        self.graph.add_node("query_node", self.query_agent.process)
        self.graph.add_node("summarize_node", self.summarization_agent.process)

        self.graph.add_edge("query_node", "summarize_node")
        self.graph.set_entry_point("query_node")

    def run(self, query):
        compiled_graph = self.graph.compile()  # Compile the graph first

        # Directly call the process method of the query agent
        query_response = self.query_agent.process(query)

        # Optionally, pass the result to the summarization agent
        summary = self.summarization_agent.process(query_response)

        return summary
