from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

# PDF processing and setup
pdfreader = PdfReader('path_to_your_pdf')
raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 800,
    chunk_overlap = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)
chain = load_qa_chain(OpenAI(), chain_type="stuff")

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    query = request.query
    docs = document_search.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    return QueryResponse(response=response)

# Unit Test endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}