#!/usr/bin/python3
"Module that lists all states from the database hbtn_0e_6_usa"
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


if __name__ == "__main__":
    engine = create_engine(
                    "mysql+mysqldb://{}:{}@localhost/{}".format(
                                        sys.argv[1], sys.argv[2],
                                        sys.argv[3]), pool_pre_ping=True
                                        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).first()
    print("{}: {}".format(query.id, query.name))

    session.close()
