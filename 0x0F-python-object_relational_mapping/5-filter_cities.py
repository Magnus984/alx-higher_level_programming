#!/usr/bin/python3
"""lists all cities of state"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute(
            """
            SELECT name FROM cities
            WHERE state_id = (
                    SELECT id FROM states WHERE name = %s
            )
            ORDER BY id ASC
            """,
            (sys.argv[4],),
    )
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
