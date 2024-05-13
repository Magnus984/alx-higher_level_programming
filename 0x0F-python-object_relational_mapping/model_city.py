#!/usr/bin/python3
"""
Models a city table in a database
"""
from sqlalchemy import Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class City(Base):
    """Defines a class named City"""
    __tablename__ = 'cities'
    id = Column(
            Integer, Sequence('state_id_seq'), primary_key=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer, ForeignKey('states.id'), nullable=False
            )
