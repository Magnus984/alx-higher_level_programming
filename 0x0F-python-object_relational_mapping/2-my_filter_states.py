#!/usr/bin/python3
"""
Filters output based on name
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )
    cur = db.cursor()
    myQuery = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id"
    cur.execute(myQuery.format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
