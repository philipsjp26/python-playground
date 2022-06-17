
from typing import Optional, Any
from pydantic import BaseModel


class BaseResponse(BaseModel):
    messages: str
    data: Optional[Any] = None

