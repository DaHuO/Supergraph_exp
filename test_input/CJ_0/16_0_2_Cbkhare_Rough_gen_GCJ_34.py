from sys import stdin as Si
from math import sqrt; from itertools import count, islice
from itertools import permutations as P

if __name__=='__main__':
    n = int(Si.readline())
    for i in range(1,n+1):
        S = Si.readline().strip('\n')
        sd = ['1' if s=='+' else '0' for s in S]
        if sum([int(x) for x in sd])==len(sd):   print('Case #%d: %d'%(i,0))
        else:
            count = 0 
            def reverse(S):
                S = S[::-1]
                Sr = ['1' if s=='0' else '0' for s in S]
                return Sr

            def backdoor(_S):
                count = 0 
                if '0'in _S and _S[0]=='1':
                    i = 0 
                    while '1'==_S[i]:   _S[i]='0';i+=1
                    count+=1

                dev_stack = []
                if '0' in _S:
                    while '0' in _S: dev_stack.append(_S.pop(0))
                    count+=1 
                    _S = reverse(dev_stack)+_S

                if '0' in _S:   count+=backdoor(_S)

                return count 
            
            print('Case #%d: %d'%(i,backdoor(sd)))
