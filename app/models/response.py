
from typing import Optional, Any
from pydantic import BaseModel
from ..entities import *

class BaseResponse(BaseModel):
    messages: str
    data: Optional[Any] = None

