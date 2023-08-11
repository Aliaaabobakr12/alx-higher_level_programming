#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    a = argv[1]
    b = argv[3]
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if (argv[2]) == "+":
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
            exit(0)
        elif (argv[2]) == "-":
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
            exit(0)
        elif (argv[2]) == "*":
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
            exit(0)
        elif (argv[2]) == "/":
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
