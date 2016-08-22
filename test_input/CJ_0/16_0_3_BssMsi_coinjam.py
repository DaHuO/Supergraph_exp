
def ffactor(n):
    if n%2==0:
        return 2
    else:
        for i in range(3,int(n**0.5),2):
            if n%i==0:
                return i
                break
def isprime3(n):
    ctr=True
    if n == 2:
        return True
    if n < 2 or n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            ctr= False
            break
    if ctr==False:
        return False
    else:
        return True
f=open("3_small.in")
L=f.readlines()
f.close()
T=int(L[0])
fw=open("3_small.out","w")
for i in range(1,T+1):
    l,n=map(int,L[i].split())
    R=[]
    n2=0
    for p in range(l-2):
        n2+=(2**p)
    j=0
    while j<n2:
        temp=bin(j)[2:]
        while len(temp)<l-2:
            temp="0"*(l-2-len(temp))+temp
        st="1"+temp+"1"
        u=2
        while u<11:
            No=int(st,u)
            if isprime3(No)==True:
                ctr=False
                break
            else:
                ctr=True
            u+=1
        if ctr==True:
            result=st
            h=1
            while h<10:
                fac=ffactor(int(st,h+1))
                result=result+" "+str(fac)
                h+=1
            R.append(result)
            if len(R)>=n:
               break
        j+=1
    fw.write('Case #%d: ' % i)
    fw.write('\n')
    for g in range(n):
        fw.write('%s' % R[g])
        fw.write('\n')
fw.close()



        
