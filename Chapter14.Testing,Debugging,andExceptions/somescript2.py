#!/usr/bin/env python3

import sys 
import csv 

def main(filename):
    with open(filename) as f:
        for row in csv.reader(f):
            print(row)

if __name__ == '__main__':
    main(sys.argv[1])
