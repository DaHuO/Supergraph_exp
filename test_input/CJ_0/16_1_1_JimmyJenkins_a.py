# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:50:14 2016

@author: James
"""

import sys
import os
from collections import deque

def make_answer(S):
    final_word = deque([S[0]])
    for char in S[1:]:
        for next_char in final_word:
            if char > next_char:
                final_word.appendleft(char)
                break
            if char < next_char:
                final_word.append(char)
                break
        else:
            final_word.append(char)
    return ''.join(final_word)
    
def rdln(txtin):
    return txtin.readline().strip()

def file_io():
    file_names = 'a'
    with open(''.join([file_names, '.in'])) as txtin, open(''.join([file_names, '.out']), 'w') as txtout:
        case_count = int(rdln(txtin))
        for i in range(case_count):
            S = rdln(txtin)
            answer = make_answer(S)
                                
            str_out = str(answer)
            txtout.write(''.join(['Case #', str(i + 1), ': ']))
            txtout.write(str_out)
            txtout.write('\n')
    osCommandString = ''.join(['notepad.exe ', file_names, '.out'])
    os.system(osCommandString)

def main():
    """Main"""
    file_io()

if __name__ == '__main__':
    sys.exit(main())
