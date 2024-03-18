#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


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

        # Create a Session
        session = Session()

        # Query all City objects and display them
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            state_name = session.query(State).filter(
                State.id == city.state_id).first().name
            print("{}: ({}) {}".format(state_name, city.id, city.name))

        # Close the session
        session.close()

    except Exception as e:
        print("An error occurred:", e)
