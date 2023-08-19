#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    username = '{}'.format(sys.argv[1])
    password = '{}'.format(sys.argv[2])
    db = '{}'.format(sys.argv[3])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
