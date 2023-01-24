#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        value = fct(*args)
        return value
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
