#!/usr/bin/python3
"""
Module that creates the State “California” with the City
“San Francisco” from the database
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

    Base.metadata.create_all(engine)

    mySessionMaker = sessionmaker(bind=engine)
    mySession = mySessionMaker()

    mySession.add(City(name="San Francisco", state=State(name="California")))
    mySession.commit()
    mySession.close()
