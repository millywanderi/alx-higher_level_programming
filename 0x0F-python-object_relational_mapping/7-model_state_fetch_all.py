#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session, sessionmaker

    username = '{}'.format(sys.argv[1])
    password = '{}'.format(sys.argv[2])
    db = '{}'.format(sys.argv[3])
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db),
                           pool_pre_ping=True)

    sessionMaker = sessionmaker(bind=engine)
    mySession = sessionMaker()
    for state in mySession.query(State).order_by(State.id):
        print("{}:{}".format(state.id, state.name))
    mySession.close()
