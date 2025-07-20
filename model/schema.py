from fastapi import Body
from typing import Annotated
from pydantic import BaseModel

class RequestPayload(BaseModel):
    user_query:Annotated[str, Body(..., description="user request")]
    
class RequestResponse(BaseModel):
    bot_response:Annotated[str, Body(..., description="user request")]