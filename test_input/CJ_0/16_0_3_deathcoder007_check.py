from random import randint
import math
def fun(N):
    if N>1 :
        for _ in xrange(5):
            Num=randint(1,N-1)
            if pow(Num,N-1,N)!=1:
                return False
        return True
    return False
def value(z,j):
    l=len(z)-1
    s=0
    for i in z:
        s+=(j*int(i))**l
        l-=1
        pass
    return s
    pass
def hell(z):
    w=[]
    for j in range(2,11):
        x=value(z,j)
        if fun(x)== False:
            if x%2==0:
                w.append(2)
            elif x%3==0:
                w.append(3)
            else:
                i=6
                ff=int(math.sqrt(x))+1
                while i<3333334:
                    if x%(i-1)==0:
                        w.append(i-1)
                        break
                    elif x%(i+1)==0:
                        w.append(i+1)
                        break
                    i+=6
        else :
            break
    return w
def main():
    for k in range(1,input()+1):
        x=raw_input().split(' ')
        print ('Case #'+str(k)+':')
        c=int(x[0])
        i=0
        ff=(2**c)-2
        c=0
        while i<ff :
            if c==int(x[1]):
                break
            s=bin(i)[2:]
            z='1'+'0'*(int(x[0])-2-len(s))+s+'1'
            w=hell(z)
            #print w
            if len(w)==9:
                print (z+' '+' '.join(str(j) for j in w))
                c+=1
            i+=1
            pass
main()