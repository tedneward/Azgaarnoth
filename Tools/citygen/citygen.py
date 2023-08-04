#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as etree
import os
import sqlite3
import sys

# This script takes the CSV from the Azgaar tool and fleshes out cities
# ("burbs") with some greater detail. Honestly, really should only need
# to be run once across all the cities in Azgaarnoth, and generate a ton
# of detail pages into /Cities, but I don't know yet if I'll want to
# re-run for particular cities or not.

