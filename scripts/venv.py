#!/usr/bin/env python
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage virtual enviroment.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i' ,"--init", action="store_true",help='Initialize virtual enviroment')
    group.add_argument('-u' ,"--update", action="store_true",help='Update virtual enviroment')
    group.add_argument('-c' ,"--clear", action="store_true",help='Delete virtual enviroment')

    args = parser.parse_args()
    print args
