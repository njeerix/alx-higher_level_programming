#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """Lists all cities of a state"""
    try:
        # Connect to MySQL server rnning on localhost at port 3306
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        # Create a cursor object using cursor() method
        cursor = db.cursor()
        # Execute SQL query to select all cities of the given state
        cursor.execute("SELECT cities.name FROM cities JOIN states "
                       "ON cities.state_id = states.id WHERE "
                       "states.name = %s ORDER BY cities.id", (state_name,))
        # Fetch all rows from the result set
        rows = cursor.fetchall()
        # Display results
        cities = ', '.join(row[0] for row in rows)
        print(cities)
        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MSQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format
              (sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    filter_cities(username, password, database, state_name)
