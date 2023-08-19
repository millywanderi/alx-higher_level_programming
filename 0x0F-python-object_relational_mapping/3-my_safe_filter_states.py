#!/usr/bin/python3
"""
Module that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, safe from MySQL injections!
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

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    myData = curs.fetchall()
    for row in myData:
        print(row)
