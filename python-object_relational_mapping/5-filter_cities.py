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
        db=argv[3], charset='utf8'
        )

    "Start the cursor"
    cur = db.cursor()

    "Execute the query"
    cur.execute(
        """
        SELECT cities.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s ORDER BY cities.id ASC
        """, (argv[4],)
    )
    rows = cur.fetchall()

    output = []
    "Print the rows of the table"
    for row in rows:
        output.append(row[0])
    print(", ".join(output))

    "Close all cursors"
    cur.close()
    "Close all databases"
    db.close()
