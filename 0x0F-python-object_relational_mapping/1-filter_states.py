#!/usr/bin/python3
""" script that lists all states with a name starting with N (upper N)\
        from the database hbtn_0e_0_usa:"""

import MySQLdb
from sys import argv


def RunScript():
    """ Function that uses to run the script """

    config = {
        'host': 'localhost',
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
        'charset': 'utf8'
        }

    db = MySQLdb.connect(**config)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    RunScript()
