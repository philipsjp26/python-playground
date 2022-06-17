from ..controller.role import RoleController
from ..models.response import BaseResponse
from ..models.schemas import RoleBase as RoleBaseSchemas
from fastapi import APIRouter, Response

subroute = APIRouter()


@subroute.post("/", response_model=BaseResponse)
def create_role(response: Response, role: RoleBaseSchemas):
    roles, messages, status_code = RoleController.create_role(role)
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": roles})


@subroute.get("/", response_model=BaseResponse)
def get_all(response: Response):
    roles, messages, status_code = RoleController.get_all()
    response.status_code = status_code
    return BaseResponse(**{"messages": messages, "data": roles})


