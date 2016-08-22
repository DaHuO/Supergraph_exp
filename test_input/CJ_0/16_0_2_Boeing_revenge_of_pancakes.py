#!/bin/python
import sys
def nb_flip(pancakes):
    if all(pancakes):
        return 0
    else:
        if pancakes[-1]:
            tmp = pancakes[:-1]
            return nb_flip(tmp)
        else:
            if pancakes[0]:
                idx = pancakes.index(False)
                for j in range(idx):
                    pancakes[j] = False
                tmp = map(lambda x: not x, pancakes[::-1])
                return 2 + nb_flip(tmp)
            else:
                tmp = map(lambda x: not x, pancakes[::-1])
                return 1 + nb_flip(tmp)
if __name__ == '__main__':
    input_name = sys.argv[1] 
    output_name = sys.argv[2] 
    f = open(input_name, 'r')
    f2 = open(output_name, 'w')
    nb_cases = int(f.readline().strip())
    for i in range(1, nb_cases+1):
        print 'case ' + str(i)
        pancakes = map(lambda x: x == '+', f.readline().strip())
        nb = nb_flip(pancakes)
        f2.write('Case #' + str(i) + ': ') 
        f2.write(str(nb) + '\n')
    f.close()
    f2.close()
