#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

def list_cities(username, password, database):
    """Lists all cities from the database"""
    try:
        # Conect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(host="localhost", user=username, passwd=password,db=database, port=3306)
        # Create a cursor object using cursor() method
        cursor = db.cursor()
        # Execute SQL query to select all cities sorted by cities.id
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER bY cities.id")
        # Fetch all ows from the result set
        rows = cursor.fetchall()
        # Display results
        for row in rows:
            print(row)
        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1:]
    list_cities(username, password, database)
