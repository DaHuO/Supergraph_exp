def slv(lst):
    if (len(lst) <= 1):
        return lst
    pos = 0
    val = lst[0]
    for k in range(1,len(lst)):
        if lst[k] >= val:
            val = lst[k]
            pos = k
    
    res = []
    if (pos == len(lst)-1):
        res = [val] + slv(lst[0:pos]) 
    elif (pos == 0):
        res = [val] + lst[pos+1:]
    else:
        res = [val] + slv(lst[0:pos]) + lst[pos+1:]
        

    return res
        

f = open('C:\\study\\gjam\\jam2016\\A-small-attempt0.in')
f_out = open('C:\\study\\gjam\\jam2016\\res.txt','w+')

T = int(f.readline())

for i in range(T):
    L = list(f.readline())
    if (i < T-1):
        L = L[0:len(L)-1]

    L = slv(L)    
    
    res = ''.join(L)
    f_out.write("Case #"+str(i+1)+": "+res+'\n')

f.close()
f_out.close()