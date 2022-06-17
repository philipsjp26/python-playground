from ..models.models import Role as RoleModel
from ..config.database import session
from ..models.schemas import RoleBase
from fastapi import status


class RoleController:
    @staticmethod
    def create_role(role: RoleBase):
        try:
            role_is_exist = session.query(RoleModel).filter_by(
                name=role.name
            ).first()
            if role_is_exist:
                return role_is_exist, "Role already exists", status.HTTP_200_OK
            roles = RoleModel(
                name=role.name,
                created_at=role.created_at
            )
            session.add(roles)
            session.commit()
            session.refresh(roles)
            messages = "Role created"
            return roles, messages, status.HTTP_201_CREATED
        except Exception as e:
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR

    @staticmethod
    def get_all():
        try:
            roles = session.query(RoleModel).with_entities(
                RoleModel.id, RoleModel.name
            ).all()
            if roles is None:
                return None
            messages = "Success retrieve data"

            return roles, messages, status.HTTP_200_OK
        except Exception as e:
            return None, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR
