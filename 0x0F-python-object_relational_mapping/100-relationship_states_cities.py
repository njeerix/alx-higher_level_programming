#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    try:
        # Create the connection engine
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]))

        # Bind the engine to the Base class
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session
        session = Session()

        # Create the State "California" with City "San Francisco"
        new_state = State(name="California", cities=[City(name="San Francisco")])
        session.add(new_state)
        session.commit()

        # Close the session
        session.close()

    except Exception as e:
        print("An error occurred:", e)
