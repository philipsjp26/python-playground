from .routes.agent import subroute as AgentRoutes
from .routes.role import subroute as RoleRoutes
from fastapi import FastAPI
API: FastAPI = FastAPI()


API.include_router(
    AgentRoutes,
    prefix='/agents',
    tags=['Agents']
)

API.include_router(
    RoleRoutes,
    prefix="/roles",
    tags=['Roles']
)
