# RAG FastAPI Assignment

This project implements a **Retrieval-Augmented Generation (RAG)** system using **FastAPI** for serving the API, **Sentence Transformers** for text embeddings, and **ChromaDB** for efficient document storage and retrieval. The system allows for ingesting documents and querying them based on a user-provided text query.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <https://github.com/gitland08/RAG_FastAPI_Assignment.git>
    cd RAG_FastAPI_Assignment
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - **Windows**:  
      ```bash
      .\env\Scripts\activate
      ```
    - **macOS/Linux**:  
      ```bash
      source env/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install fastapi uvicorn chromadb sentence-transformers python-magic pdfminer.six python-docx
    ```

## Running the FastAPI Application

1. **Start the server**:
    ```bash
    uvicorn main:app --reload
    ```
    The app will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **POST /ingest_document/**: Upload documents in `.txt`, `.pdf`, or `.docx` format. This endpoint processes the document, generates embeddings, and stores the data in ChromaDB.
- **POST /query_document/**: Query the documents by providing a text query. The system will return the most relevant documents based on semantic similarity.

## Example Usage

- **Upload documents**: Send a `POST` request to **/ingest_document/** with files.
- **Query documents**: Send a `POST` request to **/query_document/** with a query string to retrieve similar documents.

## Stopping the Server

To stop the server, press **Ctrl+C** in your terminal.

## Deactivating the Virtual Environment

When done, deactivate the virtual environment:
```bash
deactivate


## Usage

To run the FastAPI server:
```bash
uvicorn main:app --reload
