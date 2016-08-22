
# coding: utf-8

# In[ ]:

num = int(raw_input())
data = []
for i in range(num):
    data.append(raw_input())


# In[10]:

def pro_a(S):
    N = S[0]
    lenS = len(S)
    for i in range(1, lenS):
        if S[i] >= max(N):
            N = S[i] + N
        else:
            N = N + S[i]
    #print N
    return N

# In[ ]:

for i in range(num):
    print 'Case #{}: {}'.format(i+1, pro_a(data[i]))

