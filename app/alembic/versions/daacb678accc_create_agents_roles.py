"""create_agents_roles

Revision ID: daacb678accc
Revises: ef8b219bb5e0
Create Date: 2022-06-17 12:27:35.663804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = 'daacb678accc'
down_revision = 'ef8b219bb5e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'agents_roles',
        sa.Column('role_id', sa.Integer, ForeignKey('roles.id')),
        sa.Column('agents_id', sa.Integer, ForeignKey('agents.id'))
    )


def downgrade() -> None:
    op.drop_table('agents_roles')
