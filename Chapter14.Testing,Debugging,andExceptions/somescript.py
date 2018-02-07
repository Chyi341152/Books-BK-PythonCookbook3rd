#!/usr/bin/env python3

import sys 
import csv 

with open(sys.argv[1]) as f:
    for row in csv.reader(f):
        print(row)

