from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os

router = APIRouter()

class ChatQuery(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_assistant(query: ChatQuery):
    try:
        # 1. Initialize Google Services
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        # Use 'gemini-1.5-flash' for the best free-tier performance
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

        # 2. Setup Vector Store (768 dimensions)
        vectorstore = PineconeVectorStore(
            index_name=os.getenv("drone-index"), 
            embedding=embeddings,
            pinecone_api_key=os.getenv("pcsk_69hkAi_NW7SWDY4sGZDGygDhE3KjinEJ48Aa3TdXXpNWYy8xVjmMj19aGgTMnG4MwcZFGa")
        )

        # 3. Search for context
        docs = vectorstore.similarity_search(query.message, k=3)
        context = "\n".join([d.page_content for d in docs])

        # 4. Construct Prompt
        prompt = f"""
        You are an official Indian Drone Intelligence Assistant. 
        Answer ONLY using the provided context. If the answer isn't there, say 'I don't know.'
        
        Context: {context}
        User Question: {query.message}
        """

        # 5. Get Answer
        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "sources": [d.metadata.get("source", "Unknown") for d in docs]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Google AI Error: {str(e)}")