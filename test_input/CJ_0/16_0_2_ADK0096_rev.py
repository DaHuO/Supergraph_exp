s = ''
n = ''
l = []
num = 0
def inp():
    global s,n
    num = int(input())
    for i in range(num):
        s = input()
        n = ''
        for x in s:
            if(x=='-'):
                n+='0'
            else:
                n+='1'
        l.append(n)
    for i in range(num):
        print("Case #",i+1,": ",solve(l[i]),sep="")
        
def flip(n,s,e):  #s - start e - end
    p =''
    for i in range(0,s):
        p+=n[i]

    for i in range(e,s-1,-1):
        if(n[i]=='0'):
            p+='1'
        else:
            p+='0'
    for i in range(e+1,len(n)):
        p+=n[i]

    #print(" P : ",p)
    return p
        
def solve(n):
    i = 0
    s = 0
    be = ''
    if(n=='0'):
        return 1
    while(n.count('0') != 0):

        be = n
        if(n[len(n)-1] == '0' and n[0] != '1'):
            n = flip(n,0,len(n)-1)
            if(be == n):
                #print(be)
                #print(n)
                #print("SAME AFTER WHOLE FLIP")
                break
            else:
                s+=1
                #print(n)
                continue

        # find max chain
        c = 0
        while(n[c] == n[c+1]):
            c+=1
        n = flip(n,0,c)
        s+=1
        if(be == n):
            #print(be)
            #print("SAME")
            break
        i+=1
        #print(n)
    return s
inp()
