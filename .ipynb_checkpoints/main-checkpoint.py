from fastapi import FastAPI, Request
import time
from sentence_transformers import SentenceTransformer, util

from huggingface_hub import snapshot_download
model_dir = snapshot_download(repo_id="sentence-transformers/multi-qa-MiniLM-L6-cos-v1")

model = SentenceTransformer('/home/jovyan/.cache/huggingface/hub/models--sentence-transformers--multi-qa-MiniLM-L6-cos-v1/snapshots/2ad254dbef118e9d73b90b0797a1632cb455fedf', device='cuda')



app = FastAPI()

@app.get("/.well-known/live")
async def check_live():
    return status.HTTP_204_NO_CONTENT

@app.get("/.well-known/ready")
async def check_ready():
    return status.HTTP_204_NO_CONTENT

@app.get("/meta")
async def get_model_meta():
    model_meta = {
        "name": "sentence-transformers/multi-qa-MiniLM-L6-cos-v1",
        "version": "1.0",
        "description": "Your model description",
        "author": "Your name",
        "created_at": "2023-06-21"
    }
    return model_meta

@app.post("/vectors/")
async def embed(request: Request):
    payload = await request.json()
    query = payload["text"]

    start_time = time.time()
    query_embedding = model.encode(query).tolist()
    end_time = time.time()
    inference_time = end_time - start_time
    
    response_data = {
        "text": query,
        "vector": query_embedding,
        "dim": len(query_embedding),
        "ms": inference_time * 1000
    }
    return response_data
