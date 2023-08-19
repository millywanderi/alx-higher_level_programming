#!/usr/bin/python3
"""
Module that lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN\
                states ON state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    myData = cur.fetchall()
    cities = ', '.join(city[0] for city in myData)

    print(cities)
    cur.close()
    db.close()
