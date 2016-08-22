import numpy as np
def invert(num, pos):
    arr = []
    if num == 0:
        arr = [0]
    else:
        while (num > 0):
            arr += [num%2]
            num = num/2
    if (len(arr)<pos):
         arr += [0]*(pos-len(arr))
    arr = np.array(arr)
    arr = np.concatenate((1-arr[pos-1::-1],arr[pos:]))
    arr = np.array([arr[i]*2**i for i in range(len(arr))])
    return int(arr.sum())
    

fin = open("B-small-attempt1.in")
fout = open("B-small-attempt1.out","w")
trials = int(fin.readline())

for T in xrange(trials):
    s = fin.readline()
    s = s.strip()
    
    pk = 0
    for i in xrange(len(s)):
        pk += int(s[i]=='+') * 2**i
        
    pancakes = {2**(len(s))-1 : 0}
    
    L = len(s)
    step = 0
    flag = (pk==pancakes.keys()[0])
    
    while not flag:
        step += 1
        
        for cake in pancakes.keys():
            for i in range(L):
                newcake = invert(cake, i+1)
                if newcake == pk:
                    flag = True
                    break
                if not newcake in pancakes.keys():
                    pancakes[newcake] = step
    fout.write("Case #{0}: {1}\n".format(T+1,step))
                    
fin.close()
fout.close()
