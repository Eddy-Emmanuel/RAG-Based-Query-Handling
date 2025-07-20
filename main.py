from fastapi import FastAPI
import os
import sys
import uvicorn
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from endpoint_router import rag_endpoint 

app = FastAPI(root_path="/ai")

app.include_router(rag_endpoint.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
