#!/usr/bin/python3
"""
Module that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    state_name = sys.argv[4]
    found = 0
    for state in session.query(State).\
            filter(State.name == state_name).order_by(State.id):

        if state:
            print("{}".format(state.id))
            found = 1
        else:
            print("Not found")

    session.close()
