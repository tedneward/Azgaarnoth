#!/usr/bin/env python3

import argparse
import os
import random
import traceback
import types

quiet = False
verbose = False

def error(*values):
    print(*values)

def warn(*values):
    if not quiet:
        print("WARNING: ", end='')
        print(*values)

def log(*values):
    if verbose and not quiet:
        print(*values)

def main():
    global verbose
    global quiet

    parser = argparse.ArgumentParser(
        prog='lifepath',
        description='NPC LifePath Generator: A tool for generating life path events for creatures/NPCs',
        epilog='Written in Python with love'
	)

    parser.add_argument('-verbose', choices=['quiet', 'verbose'])
    parser.add_argument('-version', action='version', version='%(prog)s 0.1')
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbose != None:
        if args.verbose == 'verbose':
            verbose = True
        elif args.verbose == 'quiet':
            quiet = True



if __name__ == '__main__':
	main()
