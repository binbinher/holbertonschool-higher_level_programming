#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves all states
from the specified database. The results are printed in ascending
order by state ID.
"""
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: ./0-get_all_states.py <mysql username> <mysql password> <database name>")
    sys.exit(1)

"""Get arguments from command line"""
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database = sys.argv[3]

"""connect to MYSQL"""
db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database)
cursor = db.cursor()

"""Execute the SQL query to retrieve all states"""
cursor.execute("SELECT * FROM states ORDER BY id")
results = cursor.fetchall()
for row in results:
    print(row)

"""Close the cursor and database connection"""
cursor.close()
db.close()
