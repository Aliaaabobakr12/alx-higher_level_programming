#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (TypeError, ValueError) as e:
       print("Expection: {}".format(e), file = sys.stderr)
       return None
