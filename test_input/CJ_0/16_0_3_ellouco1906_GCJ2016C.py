#2016C-example
#2016C-small-attempt0
#2016C-large

import math

def divisor(numero):
    div=1
    for i in range(2,1+math.ceil(math.sqrt(numero))):
        if numero%i == 0:
            div=i
    return div

def numBase(string,base):
    resp=0
    exp=0
    for letter in string[::-1]:
        if letter=='1':
            loc=1
        elif letter=='0':
            loc=0
        resp=resp+loc*(base**exp)
        exp=exp+1
    return resp

in_file = open('2016C-example2.in','r')
out_file = open('2016C-example2.out','w')
num = int(in_file.readline())
print(num)
for i in range(0,num):
    d = 'Case #'+str(i+1)+':'
    print(d)
    out_file.write(d+'\n')
    n,m = map(int,in_file.readline()[:-1].split())
    limiteMin=2**(n-1)+1
    limiteMax=2**n
    print(n)
    print(m)
    print(limiteMin)
    print(limiteMax)
    respostas=1
    for j in range(limiteMin,limiteMax):
        if respostas>m:
            break
        use=True
        st=bin(j)[2:]
        if st[-1:]=='1':
            print(st)
            resp=''
            for k in range(2,11):
                convert=numBase(st,k)
                div=divisor(convert)
                print(k, convert,div)
                if div==1:
                    use=False
                    break
                else:
                    resp=resp+' '+str(div)
            if use:
                e=st+resp
                #print(respostas)
                print(e)
                out_file.write(e+'\n')
                respostas=respostas+1
out_file.close()
in_file.close()


