#!/usr/bin/python3
"""
This script lists all states from database using MySQL
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    my_data = cursor.fetchall()

    for row in my_data:
        print(row)

    cursor.close()
    db.close()
