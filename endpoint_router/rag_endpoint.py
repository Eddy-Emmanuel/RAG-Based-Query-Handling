import sys
import os
from fastapi import APIRouter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model.schema import RequestPayload, RequestResponse
from utils.rag_utils import doc_retriever_chain

router = APIRouter(prefix="/ai", tags=["RAG"])

@router.post(path="/rag/", response_model=RequestResponse)
async def RAG(user_query:RequestPayload):
    return RequestResponse(bot_response=doc_retriever_chain.invoke({"query":user_query.user_query})["result"])