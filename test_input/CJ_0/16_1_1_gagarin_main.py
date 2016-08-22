#!/usr/bin/env python3

import os
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import sys

# return dict
def read(filename):
    if not filename:
        print('Error: invalid file name')
        return None
    filename=filename.strip()
    if filename[0] == '~':
        filename = os.path.expanduser(filename)
    if not os.path.isfile(filename):
        return None
    file = open(filename, 'r')

    for line in file:
        line = line.strip()
        if not line:
            continue
        yield line

def open_file(filename,mode='r'):
    if not filename:
        print('Error: invalid file name')
        return None
    filename=filename.strip()
    if filename[0] == '~':
        filename = os.path.expanduser(filename)
    if mode == 'r' and  not os.path.isfile(filename):
        return None
    return open(filename, mode)

def imprime_saidas():
    infile = open('../data/spam_train.txt','r')
    outfile = open('saidas.log','w')
    for line in infile:
        outfile.write(line[0]+'\n')
    infile.close()
    outfile.close()

def main(infilename,outfilename):
    infile = open_file(infilename)
    outfile = open_file(outfilename, 'w')

    try:
        T = int(infile.readline())
    except:
        print('error converting string to int')
        sys.exit(1)
    # print(T)
    i = 1
    for line in infile:
        word = line.strip()
        # print(line)
        out = ''
        end = 'A'
        for letter in word:
            # print(letter)
            if end > letter:
                out += letter
            else:
                out = letter + out
            end = out[0]
        # print('Case #',end='')
        # print(i,end='')
        # print(':', out)
        outfile.write('Case #' + str(i) + ': ' + out + '\n')
        i += 1



if __name__ == '__main__':
    infilename = ''
    outfilename = ''
    if len(sys.argv) > 1:
        infilename = sys.argv[1]
    else:
        print('usage:', sys.argv[0], 'filename_input [filename_output]')
        sys.exit(1)
    if len(sys.argv) > 2:
        outfilename = sys.argv[2]
    # print('outfile:', outfilename)
    main(infilename,outfilename)
else:
    pass
