#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” \
        to the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(State(name="Louisiana"))
    state = session.query(State).filter_by(name="Louisiana").first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.commit()
    session.close()
