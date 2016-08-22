import itertools
import math

r=open('result.txt', 'w')

def test(t):
    t=''.join(t)
    res=[]
    for i in range(2, 11):
        tmp=long(t, i)
        j=2
        t1=math.sqrt(tmp)
        while j<t1:
            if tmp%j==0:
                res.append(j)
                break
            j+=1

    if len(res)==9:
        return res
    else:
        return -1

tmp=['1','0']
cnt=0
l=16
r.write('Case #1: \n')

for p in itertools.product(tmp, repeat=l-2):
    t=list(p)
    t.insert(0, '1')
    t.append('1')
    rs=test(t)
    ts=0
    if rs!=-1 and cnt<50:
        length=len(rs)
        while ts<length:
            rs[ts]=str(rs[ts])
            ts+=1

        r.write(''.join(t)+' '+' '.join(rs)+'\n')
        cnt+=1

    
