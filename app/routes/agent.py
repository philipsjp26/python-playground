from fastapi import APIRouter, Response
from typing import List


from ..controller.agent import AgentController

from ..models.response import BaseResponse
from ..models.schemas import AgentBase as AgentBaseSchemas

from ..interface import IAgentList
subroute = APIRouter()


@subroute.get("/", response_model=BaseResponse)
def get_all(response: Response):

    agents, messages, status_code = AgentController.get_all()
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": agents})


@subroute.get("/{privy_id}", response_model=BaseResponse)
def get_by_privy_id(privy_id: str, response: Response):
    agents, messages, status_code = AgentController.get_by_privy_id(privy_id)
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": agents})


@subroute.post("/", response_model=BaseResponse)
def create_agent(agent: AgentBaseSchemas, response: Response):
    agents, messages, status_code = AgentController.create_agent(agent)
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": agents})


@subroute.delete("/{id}", response_model=BaseResponse)
def destroy(id: int, response: Response):
    agents, messages, status_code = AgentController.destroy(id)
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": agents})
