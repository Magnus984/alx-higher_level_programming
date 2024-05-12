#!/usr/bin/python3
"""
Prints the State object with the name passed as
argument from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for instance in session.query(State).order_by(State.id):
        if instance.name == sys.argv[4]:
            print(instance.id)
            found = True
            break
    if found is False:
        print("Not found")
