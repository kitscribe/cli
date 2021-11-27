#!/usr/bin/env python3

from classes import TaskManager
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add')
parser.add_argument('-l', '--list', action='store_true')
parser.add_argument('-rm')
args = parser.parse_args()


if __name__ == '__main__':
    manager = TaskManager()
    manager.create_table()

    if args.rm:
        manager.remove(args.rm)

    if args.add:
        manager.create(args.add)

    if args.list:
        manager.list()
