import math,random

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))

def get_factor(x):
    for i in xrange(2, int(math.sqrt(x) + 1)-1):
        if x % i == 0:
            return i

def remove_endlines(orignal_data):
    new_data=""
    orignal_data=orignal_data.replace('\r','')
    orignal_data=orignal_data.replace('\n','')
    if orignal_data!="":
        new_data=orignal_data
    return new_data

def gen_jam(num):
    out_data='1'
    for i in range(2,num):
        out_data+=str(random.randint(0,1))
    out_data+='1'
    return out_data

def ch_jam(num):
    out=[]
    for i in xrange(2,11):
        tmp=int(num, i)
        if not is_prime(tmp):
            out.append(tmp)
        else:
            return False,[]
    return True,out

def get_dev(inlist):
    out=[]
    for i in inlist:
        out.append(get_factor(i))
    return out

testfile=open('C-small-attempt0.in','r')
ndata=testfile.readlines()
for k in range(1,len(ndata)):
    Data=remove_endlines(ndata[k]).split()
    Numberbits=int(Data[0])
    Finalnumbers=int(Data[1])
    Firstlist=[]
    Finallist=[]
    while len(Finallist) != Finalnumbers:
        tmp=gen_jam(Numberbits)
        if not (tmp in Firstlist):
            Firstlist.append(tmp)
            tmp2,tmp3=ch_jam(tmp)
            if tmp2 == True:
                tmp4=get_dev(tmp3)
                Finallist.append([tmp,tmp4])
    print "Case #{}:".format(k)
    for i in range(len(Finallist)):
        print Finallist[i][0],
        for j in range(len(Finallist[i][1])):
            print Finallist[i][1][j],
        print ""
testfile.close() 
