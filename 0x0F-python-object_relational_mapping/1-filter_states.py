#!/usr/bin/python3

"""
Module that list all states with a name starting
with N from the database.
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE\
               name LIKE BINARY 'N%' ORDER BY states.id ASC""")

    rows = cur.fetchall()

    for row in rows:
        print(row)
