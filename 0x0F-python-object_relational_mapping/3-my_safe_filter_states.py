#!/usr/bin/python3
"""
Preventing sql injections
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
    query = "SELECT * FROM states ORDER BY states.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
