# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:13:26 2016

@author: jo
"""

l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = {}
for i, letter in enumerate(l):
    letters[letter] = i
with open('input', 'r') as f:
    with open('output', 'w') as fo:
        cases = int(f.readline())
        print cases
        for case in xrange(1,cases+1):
            fo.write('Case #' + str(case) + ': ')
            print('Case: ' + str(case))
    
            word = f.readline().strip()
            w = list(word)
            
            output = []
            output.append(w[0])
            for i in xrange(1, len(w)):
                if letters.get(output[0]) <= letters.get(w[i]):
                    output.insert(0, w[i])
                else:
                    output.append(w[i])
            output = ''.join(output)
            fo.write(str(output))           
            fo.write('\n')