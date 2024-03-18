#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    try:
        # Extracting command line arguments
        username, password, database = sys.argv[1:]

        # Create the connection engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database))

        # Bind the engine to the Base class
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the State object with id = 2 and update its name
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = "New Mexico"
            session.commit()
            print("State name update successfully.")
        else:
            print("State with id 2 not found.")

        # Close the session
        session.close()

    except Exception as e:
        print("An error occurred:", e)
