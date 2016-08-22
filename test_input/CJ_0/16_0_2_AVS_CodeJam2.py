c=0
def plus(str1):
    idx=0
    str2=''
    while(str1[idx]!='-'):
        idx+=1
        if(idx>=len(str1)):break
    for i in range(idx):
        str2+='-'
    str1=str2+str1[idx:]
    global c
    c=c+1
    return(str1)

def minus(str1):
    idx=0
    str2=''
    while(str1[idx]!='+'):
        idx+=1
        if(idx>=len(str1)):break
    for i in range(idx):
        str2+='+'
    str1=str2+str1[idx:]
    global c
    c=c+1
    return(str1)

def check(str1):
    for i in str1:
        if(i!='+'):
            return(0)
    return(1)

def flip(str1):
    if(str1[0]=='+'):
        str1=plus(str1)
        if(check(str1)):return
        else:
            flip(str1)
    else:
        str1=minus(str1)
        if(check(str1)):return
        else:
            flip(str1)

def IHP(case,str1):
     print("case #{0}: ".format(case),end='')
     if(check(str1)):print(c)
     else:
         flip(str1)
         print(c)

T=int(input())
li=[]
ct=1
if T>0:
    for i in range(T):
        li.append(str(input()))
    for i in li:
        global c
        c=0
        IHP(ct,i)
        ct+=1
