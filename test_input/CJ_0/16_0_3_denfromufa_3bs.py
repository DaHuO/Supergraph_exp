from __future__ import print_function
import sys
import numpy
from itertools import product
from sympy import isprime
SALL=False
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def getfactors(d):
    for s in product('01',repeat=d-2):
        ispr=False
        facts=list()
        for b in range(2,11):
            sf='1'+''.join(s)+'1'
            i=int(sf,b)
            if isprime(i):
                ispr=True
                break
            else:
                #if len(facts)<g+2:
                factsi=factors(i)
                factsi.remove(i)
                factsi.remove(1)
                print("binary {} base in {} = {} :".format(
                    sf, b, i), end=' ')
                while True:
                    if factsi:
                        fi=factsi.pop()
                    else:
                        if SALL:
                            break
                        else:
                            raise ValueError("Exhausted all options!")
                    if (fi not in facts) or SALL:
                        if (i % fi)==0:
                            facts.append(fi)
                            print(fi,end=' ')
                            if not SALL:
                                break
                        else:
                            print("wrong factor {} for binary {} in base {} = {}".format(
                                fi, sf, b, i))
                    #else:
                    #    print("collision")
                print()
        if (not ispr) and len(facts)==9:
            yield sf,facts

def confirmfacts(numbin,factors):
    if (len(factors)!=9):
        raise ValueError("not enough factors")
    fs=set()
    for i,f in enumerate(factors):
        if f in fs:
            raise ValueError("repeated factor")
        else:
            fs.add(f)
        n=int(numbin,i+2)
        if (n % f) != 0:
            print("wrong factor {} for binary {} in base {} = {}".format(
                                f, numbin, i+2, n))
            return False
    return True

with open(r"/home/dta/Downloads/jam/input.txt",mode='r') as f1:
    finput=f1.readlines()
T=int(finput[0])

if len(finput)!=(T+1):
    raise Exception("bad input file")
with open(r"/home/dta/Downloads/jam/output.txt",mode='w') as f2:
    for x in range(1,T+1):
        N,J=map(int,finput[x].split())
        c=0
        f2.write("Case #{x}:\n".format(x=x))
        sols=set()
        for n,f in getfactors(N):
            #if len(f)>=g+2:
            y=map(str,list(f))
            if SALL or confirmfacts(n,f):
                print(y)
            else:
                raise ValueError("some factors wrong!")
            if n in sols:
                raise ValueError("repeated solution")
            else:
                sols.add(n)
            f2.write("{n} {y}\n".format(n=n,y=" ".join(y)))
            c+=1
            if c==J:
                break