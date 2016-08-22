#!/bin/python
import sys
import numpy as np
if __name__ == '__main__':
    input_name = sys.argv[1] 
    output_name = sys.argv[2] if len(sys.argv) > 2 else input_name.split('.')[0] + '.out'
    f = open(input_name, 'r')
    f2 = open(output_name, 'w')
    nb_cases = int(f.readline().strip())
    for i in range(1, nb_cases+1):
        print 'case ' + str(i)
        f2.write('Case #' + str(i) + ': ') 
        s = f.readline().strip()
        o = []
        for l in s:
            if len(o) == 0 or l >= o[0]:
                o.insert(0, l)
            else:
                o.append(l)
        f2.write(''.join(o) + '\n')
    f.close()
    f2.close()
