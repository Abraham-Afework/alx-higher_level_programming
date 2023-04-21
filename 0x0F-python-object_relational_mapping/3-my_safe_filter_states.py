#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states \
        table of hbtn_0e_0_usa where name matches the argument.\
        that is safe from MySQL injections!"""

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
    argument = argv[4].split()
    if len(argument) == 1:
        query = "SELECT * FROM states WHERE NAME LIKE '{}'  COLLATE utf8_bin \
            ORDER BY id ASC".format(argv[4])
        db = MySQLdb.connect(**config)
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        for row in rows:
            print(row)
        cur.close()
        db.close()


if __name__ == "__main__":
    RunScript()
