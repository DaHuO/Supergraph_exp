
# coding: utf-8

# Jam Coins

# In[1]:

N = 16 #length of jam coins
J = 50 # Number to give


# In[1]:

import numpy as np
from functools import lru_cache


# In[2]:

def getValues(jamcoin):
    bases = [ np.asarray([ (b+2)**i for i in range(len(jamcoin))[::-1] ]) for b in range(9) ]
    return [ np.dot(base, list(map(int, list(jamcoin)))) for base in bases ]


# In[6]:

@lru_cache()
def getPrimes():
    table = [True] * 43333333
    for v in range(len(table)):
        if (v % 10**7 == 0):
            print(v)
        if v == 0:
            table[v] = True
        elif v == 1:
            table[v] = False
        elif (table[v]):
            j = 2 * v
            while j < len(table):
                table[j] = False
                j += v
    return table


# In[46]:

primeList = np.where(getPrimes())[0][1:]

def isPrime(x):
    for p in primeList:
        if x % p == 0:
            if x == p:
                return 0
            return p
    return 0


# In[80]:

found = 0
i = 1
while found < 50:
    i += 1
    jammer = "1"+"{0:b}".format(i).zfill(14) + "1"
    vals = list(map(isPrime, getValues(jammer)))
    if 0 not in vals:
        print(jammer + ' ' + ' '.join(map(str, vals)))
        found += 1


# In[78]:

list(vals)


# In[ ]:



