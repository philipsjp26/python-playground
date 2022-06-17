
from ..models.models import Agent as AgentModel
from ..models.models import Role as RoleModel
from ..models.schemas import AgentBase as AgentBaseSchema
from ..config.database import session
from sqlalchemy.orm import subqueryload, joinedload
from fastapi import status


class AgentController:

    @staticmethod
    def create_agent(agent: AgentBaseSchema):
        try:
            privy_id_is_exist = session.query(AgentModel).filter_by(
                privy_id=agent.privy_id).first()
            if privy_id_is_exist:
                agent = privy_id_is_exist.roles
                return agent, "Agents already exist", status.HTTP_200_OK

            role_is_exist = session.query(RoleModel).filter(
                RoleModel.id.in_(agent.roles)).all()
            if not role_is_exist:
                return None, "Role not found", status.HTTP_200_OK

            agents = AgentModel(
                name=agent.name,
                privy_id=agent.privy_id                
            )
            
            for value in role_is_exist:                
                agents.roles.append(value)

            session.add(agents)
            session.commit()
            session.refresh(agents)
            return agents, "Agents created", status.HTTP_201_CREATED
        except Exception as e:
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def get_all():
        try:
            agents = session.query(AgentModel).options(subqueryload(AgentModel.roles)).all()            
            if agents is None:
                return None

            messages = "Success retrieve data"

            return agents, messages, 200
        except Exception as e:
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def get_by_privy_id(privy_id: str):
        try:
            agent = session.query(AgentModel).filter(
                AgentModel.privy_id == privy_id).options(joinedload(AgentModel.roles)).first()
            if not agent:
                messages = "Agent not found"
                return None, messages, 200
            messages = "Success retrieve data"
            return agent, messages, 200
        except Exception as e:
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def destroy(id: int):
        try:
            agents = session.query(AgentModel).get(id)
            session.delete(agents)
            session.commit()
            session.close()
            return agents, "", 201
        except Exception as e:
            session.rollback()
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR
