import os
import sys
import uvicorn
from fastapi import FastAPI

# Add project folder path to python module search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from endpoint_router import rag_endpoint 

# Initialize fastapi app
app = FastAPI(root_path="/ai")

# Add the created route/endpoint
app.include_router(rag_endpoint.router)

# Run code if the main app is not imported anywhere else
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
