#!/usr/bin/python3

import MySQLdb
import sys

def get_all_states(username, password, database):
    # Establish connection to the database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the script is run directly
    if len(sys.argv) != 4:
        print("Usage: ./0-get_all_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to get all states
    get_all_states(mysql_username, mysql_password, database_name)
