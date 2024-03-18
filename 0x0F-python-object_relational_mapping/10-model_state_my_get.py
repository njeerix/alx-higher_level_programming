#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Extracting command line arguments
    username, password, database, state_name = sys.argv[1:]

    try:
        # Create the connection engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

        # Query the State object with the given state name
        query = session.query(State)
        state = query.filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()

    except Exception as e:
        print("An error occurred:", e)
