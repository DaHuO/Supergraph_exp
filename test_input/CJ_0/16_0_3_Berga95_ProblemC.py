
def isPrime(n):
    if n==2 or n==3: return 0
    if n%2==0 or n<2: return 2
    for i in range(3,100,2):      #int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return i    

    return 0

def check(n):
    l = []
    l2 =[]
    for x in range(2,11):
        l.append(int(n,x))
        #print l
    allnp = True
    for x in l:
        a = isPrime(x)
        #print a,x
        if a!=0:
            l2.append(a)
        else:
            return []
    return l2
            
    

#f = open("input.in", "r")
fout = open("output.out", "w")
N=32
J=501
check("1001")

j=1
s = "1"+"0"*(N-2)+"1"

fout.write("Case #1: \n")
while j<J:
    res = check(s)
    if len(res)>0:
        fout.write(s)
        fout.write(" ")
        for x in res:
            fout.write("{0} ".format(x))
        j+=1
        fout.write("\n")
        s = str(bin(int(s,2)+2))[2:]
        print s
    else:
        s = str(bin(int(s,2)+2))[2:]
fout.close()
