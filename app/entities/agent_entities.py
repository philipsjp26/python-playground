from typing import List, Union
from datetime import datetime
from pydantic import BaseModel


class OurBasedModel(BaseModel):
    class Config:
        orm_mode = True


class AgentEntity(OurBasedModel):
    id: int
    name: str
    privy_id: str    
    created_at: Union[datetime, None]
