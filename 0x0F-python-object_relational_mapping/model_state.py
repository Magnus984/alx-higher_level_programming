#!/usr/bin/python3
"""
Implementing ORM sqlalchemy
"""
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class States(Base):
    """Represents a state table in a database"""i
    __tablename__ = 'states'

    id = Column(
            Integer, Sequence('state_id_seq'), primary_key=True
            )
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
