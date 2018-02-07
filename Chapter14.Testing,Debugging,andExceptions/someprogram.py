#!/usr/local/env python3

import time 

def main():
    for i in range(1,10):
        time.sleep(0.5)
        print('{} output'.format(i))

if __name__ == '__main__':
    main()
