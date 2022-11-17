#!/usr/bin/python3
"Module that lists all states from the database hbtn_0e_0_usa"
import MySQLdb
import sys


"Condition that causes the file cannot be imported"
if __name__ == "__main__":
    argv = sys.argv

    "Connect python file to server"
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3]
        )

    "Start the cursor"
    cur = db.cursor()

    "Execute the query"
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    "Print the rows of the table"
    for row in rows:
        print(row)

    "Close all cursors"
    cur.close()
    "Close all databases"
    db.close()
