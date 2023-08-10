#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print("0")
    else:
        counter = 0
        for i in range(1, len(argv)):
            pk = int(argv[i])
            counter += pk
        print("{}".format(counter))
