import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorStore:
    def __init__(self, index_path="backend/faiss_index"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.index_path = index_path
        self.vector_store = self.load_vector_store()

    def load_vector_store(self):
        try:
            # Check if index files exist at the correct path
            faiss_file = os.path.join(self.index_path, "index.faiss")
            pkl_file = os.path.join(self.index_path, "index.pkl")

            if os.path.exists(faiss_file) and os.path.exists(pkl_file):
                # Attempt to load the FAISS index if both files exist
                return FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
            else:
                # Create a new FAISS index if files do not exist
                print("Index files not found, creating a new index...")
                texts = ["This is a default document for the FAISS index."]  # Replace with real documents
                return FAISS.from_texts(texts, self.embeddings)
        except (ValueError, RuntimeError) as e:
            print(f"Error loading index: {e}")
            # Handle errors, possibly by creating a new index
            return FAISS.from_texts([], self.embeddings)

    def add_document(self, text):
        # Create a new store from the added text and merge it with the existing vector store
        new_store = FAISS.from_texts([text], self.embeddings)
        self.vector_store.merge_from(new_store)
        self.vector_store.save_local(self.index_path)

    def similarity_search(self, query, k=5):
        # Perform similarity search on the current vector store
        return self.vector_store.similarity_search(query, k)

# Example Usage
if __name__ == "__main__":
    store = VectorStore()
    store.add_document("This is a legal document about corporate law.")
    results = store.similarity_search("corporate law", k=3)
    print(results)
