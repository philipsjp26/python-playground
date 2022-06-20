from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


from ..entities import AgentEntity


class IAgentList(BaseModel):
    messages: str
    data: AgentEntity
