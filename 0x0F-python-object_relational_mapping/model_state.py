#!/usr/bin/python3
"""
Implementing ORM sqlalchemy
"""
import sqlalchemy
from sqlalchemy import create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine(
        'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
        )

Base = declarative_base()


class States(Base):
    __tablename__ = 'states'

    id = Column(
            Integer, Sequence('state_id_seq'), primary_key=True
            )
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
