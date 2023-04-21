#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all\
        cities of that state, using the database hbtn_0e_4_usa """

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
        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id\
                = states.id WHERE states.name = '{}'  COLLATE utf8_bin \
                ORDER BY cities.id ASC".format(argv[4])
        db = MySQLdb.connect(**config)
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()

        print(", ".join(row[0] for row in rows))
        cur.close()
        db.close()


if __name__ == "__main__":
    RunScript()
