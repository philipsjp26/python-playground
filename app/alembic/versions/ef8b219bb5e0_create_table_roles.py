"""create_table_roles

Revision ID: ef8b219bb5e0
Revises: b0dce2b0ef55
Create Date: 2022-06-16 17:48:38.029952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef8b219bb5e0'
down_revision = 'b0dce2b0ef55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('roles')
