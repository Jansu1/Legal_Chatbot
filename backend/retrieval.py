from backend.vector_store import VectorStore

class Retrieval:
    def __init__(self, vector_store):
        self.vector_store = vector_store  # Properly initializing VectorStore from passed argument

    def retrieve_documents(self, query, k=5):
        return self.vector_store.similarity_search(query, k)
