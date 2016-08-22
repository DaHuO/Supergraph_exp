#!/usr/bin/python

from twiggy import quick_setup, log as l
from itertools import product
from copy import deepcopy
import random

filename="data00.txt"
outfile="out00.txt"
GROUPS=2
DATA=[]


def getData(cases):
    global DATA

    i=0
    f=open(outfile, "a+")
    for ncase in range(cases):
        rs=(ncase+1, DATA[ncase], process(DATA[ncase]) )
        l.name("getData").fields(ncase=rs[0], data=rs[1], generated=rs[2]).info("ordered")
        f.write("Case #%d: %s \n" % (rs[0], rs[2]))
    f.close()

def process(case):

    ordered=case[0]
    for ch in case[1:]:
        if ch>=ordered[0]:
            ordered=ch+ordered
        else:
            ordered+=ch

    return ordered

def main():
    global DATA

    quick_setup()
    lines=open(filename, "r").readlines()
    cases=int(lines[0].strip())
    for g in range(cases): DATA.append(lines[g+1].strip())
    lg=l.name("main")
    lg.fields(cases=cases).info("init")
    getData(cases)


if __name__ == "__main__":
    main()
