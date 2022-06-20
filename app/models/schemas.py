from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    created_at: Union[datetime, None] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")


class AgentBase(BaseModel):
    name: str
    privy_id: str
    roles: List[int]
    created_at: Union[datetime, None] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S")
