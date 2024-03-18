#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
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
        # Create the connection engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))

        # Bind the engine to the Base class
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query all State objects containing the letter 'a'
        states_with_a = session.query(State).filter(State.name.like('%a%')) \
            .all()

        # Delete the State objects containing the letter 'a'
        for state in states_with_a:
            session.delete(state)

        # Commit the changes
        session.commit()

        # Close the session
        session.close()

    except Exception as e:
        print("An error occurred:", e)
