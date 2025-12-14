from pydantic import BaseModel,Field
from typing import Any, List, Optional
from datetime import datetime

class ApiResponse(BaseModel):
    status_code:int
    message:str 
    data:Any

class MessageRequest(BaseModel):
    message: str