#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """Lists all states with a name starting with 'N'"""
    try:
        # Connect to MySQL server running on localhost at port 3306
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        # Create a cursor object using cursor() method
        cursor = db.cursor()
        # Execute SQL queryy to select all states with a name starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE
                       'N%' OR name LIKE 'n%' ORDER BY id")
        # Fetch all rows from the result set
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
    filter_states(username, password, database)
