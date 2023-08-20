#!/usr/bin/python3
"""
Module that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    mySessionMaker = sessionmaker(bind=engine)
    mySession = mySessionMaker()
    for state in mySession.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            ("\t{}: {}".format(city.id, city.name))
    mySession.close()
