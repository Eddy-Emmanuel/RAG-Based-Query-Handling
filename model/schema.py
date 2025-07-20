# import libraries
from fastapi import Body
from typing import Annotated
from pydantic import BaseModel

# Define endpoints schema's

# 1. Request schema
class RequestPayload(BaseModel):
    user_query:Annotated[str, Body(..., description="user request")]

# 2. Response schema
class RequestResponse(BaseModel):
    bot_response:Annotated[str, Body(..., description="user request")]