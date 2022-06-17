from typing import List, Union, Optional, Any
from datetime import datetime
from pydantic import BaseModel


from ..entities import *


class IAgentList(BaseModel):
    messages: str
    data: List[AgentEntity]


class IAgentDetail(BaseModel):
    message: str
    data: AgentEntity
