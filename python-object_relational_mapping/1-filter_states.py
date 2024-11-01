#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves all states
with a name starting with the letter 'N'. The results are displayed
in ascending order by state ID.
"""

import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
    sys.exit(1)

"""Get arguments from command line"""
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database = sys.argv[3]

"""connect to MYSQL"""
db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database)
cursor = db.cursor()

"""
xecute the SQL query to retrieve states 
starting with 'N'
"""
cursor.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")

"""Fetch all results"""
states = cursor.fetchall()

"""Display results"""
for state in states:
    print(state)

"""Close the cursor and database connection"""
cursor.close()
db.close()
