#!/usr/bin/env python
import os
import argparse

def init():
    pass


def clear():
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage directories for webapi project.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i' ,"--init", action="store_true",help='Initialize all folders')
    group.add_argument('-c' ,"--clear", action="store_true",help='Delete all folders.')

    args = parser.parse_args()
    print args