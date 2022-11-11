#! /usr/bin/env python

# For Python3
# Script to print uninstall infor from logs/MobileContainerManager/containermanagerd.log.0
# Author: cheeky4n6monkey@gmail.com

import sys, re
from optparse import OptionParser

def find_app(input_text):
    app = re.search(r"[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+", input_text)
    return app.group()

version_string = "sysdiagnose-mobilecontainermanager.py v2022-11-11 Version 1.1"

if sys.version_info[0] < 3:
    print("Must be using Python 3! Exiting ...")
    exit(-1)

print("Running " + version_string + "\n")

usage = "\n%prog -i inputfile\n"

parser = OptionParser(usage=usage)
parser.add_option("-i", dest="inputfile",
                  action="store", type="string",
                  help="logs/MobileInstallation/mobile_installation.log.0 To Be Searched")
(options, args) = parser.parse_args()

#no arguments given by user, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    exit(-1)

linecount = 0
hitcount = 0
with open(options.inputfile, 'r') as fp:
    data = fp.readlines()

    for line in data:
        linecount += 1

        if '[MIClientConnection uninstallIdentifiers:withOptions:completion:]' in line:
            hitcount += 1
            #print("\n" + line)
            txts = line.split()
            #print(txts, linecount)
            #print(len(txts))
            dayofweek = txts[0]
            month = txts[1]
            day = txts[2]
            time = txts[3]
            year = txts[4]
            group = txts[15]
            print(day + " " + month + " " + year + " " + time + " Removed " + group + " [line " + str(linecount) + "]" + " [" + find_app(line) + "]")

print("\nFound " + str(hitcount) + " group removal entries\n")
