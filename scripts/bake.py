#!/usr/bin/env python
import argparse

def copy():
    pass


def build():
    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage virtual enviroment.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c' ,"--copy", action="store_true",help='Initialize virtual enviroment')
    group.add_argument('-b' ,"--build", action="store_true",help='Update virtual enviroment')
    group.add_argument('-p' ,"--purge", action="store_true",help='Delete virtual enviroment')

    args = parser.parse_args()
    print args
