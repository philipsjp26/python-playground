# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


agent_roles = Table(
    'agents_roles', metadata,
    Column('role_id', ForeignKey('roles.id'), primary_key=True, index=True),
    Column('agents_id', ForeignKey('agents.id'), primary_key=True, index=True)
)

class Agent(Base):
    __tablename__ = 'agents'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    privy_id = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    roles = relationship('Role', secondary=agent_roles, backref='roles')


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    agents = relationship("Agent", secondary=agent_roles, backref='agents')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


