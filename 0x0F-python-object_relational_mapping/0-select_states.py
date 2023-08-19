#!usr/bin/python3
"""
This script lists all states from database using MySQL
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':

    dbUser = argv[1]
    dbPasswd = argv[2]
    dbName = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=dbUser,
        passwd=dbPasswd,
        db=dbName
        )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    my_data = cursor.fetchall()

    for row in my_data:
        print(row)

    cursor.close()
    db.close()
