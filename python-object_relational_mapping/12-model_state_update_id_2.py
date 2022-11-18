#!/usr/bin/python3
"Module that lists all states from the database hbtn_0e_6_usa"
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

def state():
    session = Session()

    qry = session.query(State).filter(State.id == 2).first()
    qry.name = "New Mexico"
    session.commit()
    session.close()


if __name__ == "__main__":
    engine = create_engine(
                    "mysql+mysqldb://{}:{}@localhost/{}".format(
                                        sys.argv[1], sys.argv[2],
                                        sys.argv[3]), pool_pre_ping=True
                                        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    state()
