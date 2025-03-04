import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # If Groq requires an API key

class DocumentLoader:
    def __init__(self, data_path="../data/", faiss_index_path="faiss_index"):
        self.data_path = data_path
        self.faiss_index_path = faiss_index_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    def load_pdfs(self):
        documents = []
        for file in os.listdir(self.data_path):
            if file.endswith(".pdf"):
                pdf_path = os.path.join(self.data_path, file)
                loader = PyPDFLoader(pdf_path)
                documents.extend(loader.load())
        return documents

    def process_documents(self):
        raw_docs = self.load_pdfs()

        if not raw_docs:
            print("⚠️ No PDFs found in the data directory.")
            return

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        split_docs = text_splitter.split_documents(raw_docs)

        faiss_index = FAISS.from_documents(split_docs, self.embeddings)
        faiss_index.save_local(self.faiss_index_path)
        print(f"✅ FAISS index saved at {self.faiss_index_path}")

if __name__ == "__main__":
    loader = DocumentLoader()
    loader.process_documents()
