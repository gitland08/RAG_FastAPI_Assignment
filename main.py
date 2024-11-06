from fastapi import FastAPI, UploadFile, File, HTTPException
from sentence_transformers import SentenceTransformer
from chromadb import ChromaDB, Collection
import asyncio
from typing import List
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
import os

app = FastAPI()

# Initialize the embedding model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize ChromaDB
db = ChromaDB(persist_directory='./chroma_db')
doc_collection = db.get_collection("documents")

# Utility function to extract text from different file types
async def extract_text(file: UploadFile):
    if file.filename.endswith(".txt"):
        return (await file.read()).decode("utf-8")
    elif file.filename.endswith(".pdf"):
        return pdf_extract_text(file.file)
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format")

@app.post("/ingest_document/")
async def ingest_document(files: List[UploadFile] = File(...)):
    for file in files:
        doc_text = await extract_text(file)
        
        # Generate embedding
        embedding = model.encode(doc_text)
        
        # Store in ChromaDB
        doc_id = file.filename
        doc_collection.add(doc_id, embedding, {"text": doc_text})
    
    return {"status": "Documents successfully ingested"}

@app.post("/query_document/")
async def query_document(query: str):
    # Generate embedding for query
    query_embedding = model.encode(query)
    
    # Query ChromaDB for similar documents
    results = doc_collection.query(query_embedding, k=5)
    
    if not results:
        raise HTTPException(status_code=404, detail="No similar documents found.")
    
    return {
        "query": query,
        "similar_documents": [{"text": doc["text"], "score": doc["score"]} for doc in results]
    }

