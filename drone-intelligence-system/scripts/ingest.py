import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCFknESdc5sfag5r6AyD2gmUjVLgR2ndEc"
os.environ["PINECONE_API_KEY"] = "pcsk_69hkAi_NW7SWDY4sGZDGygDhE3KjinEJ48Aa3TdXXpNWYy8xVjmMj19aGgTMnG4MwcZFGa"

from langchain_google_genai import GoogleGenerativeAIEmbeddings
# ... rest of your code ...
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings # Updated this
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

def run_ingestion():
    # --- 1. Initialize Google Embeddings ---
    # We use 'models/embedding-001', which is Google's standard embedding model
    # Change the model name to the more recent version
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    index_name = "drone-index" 

    # --- 2. Load PDF ---
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "../data/raw/Drone_Rules_2021.pdf")
    
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        return

    loader = PyPDFLoader(pdf_path)
    raw_docs = loader.load()

    # --- 3. Chunking ---
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(raw_docs)

    # --- 4. Upload ---
    print(f"Starting ingestion for {len(chunks)} chunks using Google Gemini...")
    vectorstore = PineconeVectorStore.from_documents(
        chunks, 
        embeddings, 
        index_name=index_name
    )
    print("Ingestion successful. Data is now searchable via Google AI!")

if __name__ == "__main__":
    run_ingestion()