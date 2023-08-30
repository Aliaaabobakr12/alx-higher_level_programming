#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0
    try:
        while True:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
                if count == x:
                    break
            i += 1
    except (TypeError, IndexError):
        pass
    print()
    return count
