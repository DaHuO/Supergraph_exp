#!/usr/bin/env python3
# the Last Word

from sys import argv
from time import process_time

# global variables and constants
inData = []
TEST = False # not all caps

if TEST:
    t0 = process_time()
# basic IO
def init():
    if len(argv) > 0:
        # outFile = sys.argv[2]
        global inData
        with open(argv[1], "rt") as f: # should change to read filename
            inData = f.read()

def printTest(aVariable):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

def printOutput(number, result):
    outString = 'Case #' + str(number) + ': ' + result
    print(outString)
    return outString

if TEST:
    pass

# problem-specific defs

# main
init()
dataset = inData.splitlines()
diter = iter(dataset)
T = int(next(diter))

for tt in range(1, T+1): # for each test case
    S = list(next(diter))
    word = S[0]
    for ss in S[1:]:
        if ord(ss) < ord(word[0]):
            word += ss
        elif ord(ss) > ord(word[0]):
            word = ss + word
        else: # ss = word[0]
            word1 = ss + word
            word2 = word + ss
            word = sorted([word1, word2])[-1]
    printOutput(tt, word)

if TEST:
    t = process_time() - t0
    print("elapsed_time: ", t)

# printOutput(tt, str(Ni))
    
