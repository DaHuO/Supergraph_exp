import math
def bs10t2(num, bs):
    cnvrtd_strng, modstring = "", ""
    crntnm = num
    if not 1 < bs < 37:
        raise ValueError("bs error")
    if not num:
        return '0'
    while crntnm:
        mod = crntnm % bs
        crntnm = crntnm // bs
        cnvrtd_strng = chr(48 + mod + 7*(mod > 10)) + cnvrtd_strng
    return int(cnvrtd_strng)

def ckPrm(numvp):
    zx=int(math.sqrt(numvp))+1
    for dd in range (2,zx):
        if(numvp%dd==0):
            return dd
    return 0

def bs10tn(test,bs):
    strtest=str(test)
    strtest=strtest[::-1]
    ijk=0
    abc=0
    for sd in strtest:
        abc=abc+int(sd)*math.pow(bs,ijk)
        ijk=ijk+1
    return int(abc)

filein=open("C-small-attempt2.in")
fileout=open("C-small-attepmt2.out","w")
qaz=[]
for get in filein:
    qaz.append(get.rstrip('\n'))
times=int(qaz[0])
for x in range(1,times+1):
    flag=0
    abc=qaz[x]
    abc=abc.split(" ")
    n=int(abc[0])
    j=int(abc[1])
    last=int(math.pow(2,n)-1)
    first=int(math.pow(2,n-1)+1)
    fileout.write("Case #"+str(x)+":\n")
    for z in range(first,last+1,2):
        test=bs10t2(z,2)
        bs2=bs10tn(test,2)
        bs3=bs10tn(test,3)
        bs4=bs10tn(test,4)
        bs5=bs10tn(test,5)
        bs6=bs10tn(test,6)
        bs7=bs10tn(test,7)
        bs8=bs10tn(test,8)
        bs9=bs10tn(test,9)
        bs10=test
        dvsr2=ckPrm(bs2)
        dvsr3=ckPrm(bs3)
        dvsr4=ckPrm(bs4)
        dvsr5=ckPrm(bs5)
        dvsr6=ckPrm(bs6)
        dvsr7=ckPrm(bs7)
        dvsr8=ckPrm(bs8)
        dvsr9=ckPrm(bs9)
        dvsr10=ckPrm(bs10)
        if(dvsr2!=0 and dvsr3!=0 and dvsr4!=0 and dvsr5!=0 and dvsr6!=0 and dvsr7!=0 and dvsr8!=0 and dvsr9!=0 and dvsr10!=0):
            fileout.write(str(test)+" "+str(dvsr2)+" "+str(dvsr3)+" "+str(dvsr4)+" "+str(dvsr5)+" "+str(dvsr6)+" "+str(dvsr7)+" "+str(dvsr8)+" "+str(dvsr9)+" "+str(dvsr10)+"\n")
            flag=flag+1
        if(flag==j):
            break

fileout.close()
filein.close()
        
