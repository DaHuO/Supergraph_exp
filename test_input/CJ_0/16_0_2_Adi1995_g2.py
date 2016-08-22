filein=open("B-large.in")
fileout=open("B-large.out","w")
list1=[]
for get in filein:
    list1.append(get.rstrip('\n'))
a=int(list1[0])
for x in range(1,a+1):
    b=list1[x]
    flag=0
    rslt=0
    temp='-'
    for  z in b:
        if(z=='-'):
            flag=flag+1
            if(temp=='+'):
                rslt=rslt+1
                temp='-'
        else:
            if(flag!=0):
                rslt=rslt+1
            flag=0
            temp='+'
    if(flag!=0):
        rslt=rslt+1

    zz=str(x)
    rslt=str(rslt)

    fileout.write("Case #"+zz+": "+rslt+'\n')
filein.close()
fileout.close()
