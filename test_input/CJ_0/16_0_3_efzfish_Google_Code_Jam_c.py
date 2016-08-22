
# coding: utf-8

# In[ ]:

import numpy as np


# In[83]:

T = int(raw_input())
N, J = [int(x) for x in raw_input().split(" ")]


# In[ ]:




# In[84]:

def jamcoin(x):
    lis = []
    divisorlis = []
    flag = 0
    for i in range(2,11):
        lis.append(int(x, i))
    try:
        for j in lis:
            if quasi_isprime(j)[0] == False:
                divisorlis.append(quasi_isprime(j)[1])
        flag = 1
    except:
        pass
    return(divisorlis, flag)


# In[85]:

def quasi_isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, min(10001,int(n**0.5)+1), 2):
        if n % x == 0:
            return False, x
    return True


# In[86]:

jc = 2 ** (N-1)
jclist = []
while (len(jclist) < J):
    jcbin = bin(jc)[2:]
    jamc = jamcoin(jcbin)
    if jamc[1] == 1:
        ans = [jcbin] + jamc[0]
        jclist.append(ans)
    jc += 1


# In[91]:

print 'Case #1:'
for i in range(J):
    print ' '.join(map(str, jclist[i]))


# In[ ]:




# In[ ]:



