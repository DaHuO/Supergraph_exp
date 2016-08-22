
inf=open("C:\\Users\\Anchit\\Downloads\\code jam\\test.txt")
import math
t=int(inf.readline())
output=[]

#possible_num=[]
n,m=map(int,inf.readline().split())
n1=n-2
last=(2**n1)
possible=[]
interpretation=[]
count=0
def binary(num, pre='0b', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])


def factors(n):    
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return i
            break

   # return set(reduce(list.__add__, 
    #            ([i, n//i] break for i in range(1, int(n**0.5) + 1) if n % i == 0)))

    
def dec_to_bin(num1):
    #global possible_num
    global count
    for i in xrange(0,last):
        j=binary(i,'0b',num1)
        
        #possible_num.append(j[2:])
        a=int('1'+j[2:]+'1')
       
        if count<m:
            main_fun(a)
        else:
            break



def base_convertor(num,base):
    n_str=str(num)
    result=[]
    sum1=0
    for i in n_str:
        result.append(int(i))
    for j in xrange(len(result)-1,-1,-1):
        sum1+=(result[len(result)-j-1]*(base**j))
    return sum1

def check_prime(num1):
    if(num1 == 2):
        return 1;
    if(num1%2 == 0):
        return 0;
    #for(i = 3; i*i<=n; i+=2):
    i=3
    flag=1
    n1=math.sqrt( num1 )+1
    while i<=n1:       
        if(num1%i == 0):
            flag=0;
            break
        i+=2
    if flag==1:
        return 1
    else:
        return 0

'''    a=2
    f=1
    while a < num1 :
      if num1%a!=0:
        a=a+1
      else:
        a=(num1)+1
        f=0

    if f==0:
        return 0
    else:
        return 1
   
    
    if num1==2:
        return 1
    else:
        count=2
        for i in range(2,num1):
            count+=1
            if num1%i==0:
                return 0
                break
        if count==num1:
            return 1
'''     


remove_list=[]
def main_fun(num):
    global interpretation
    global possible
    global count
    global remove_list
    if count<m:
        
        temp=[]
        f=0
        base_no=base_convertor(num,2)
        cp=check_prime(base_no)
        
        if cp==0:
            
            temp.append(base_no)
            for j in range(3,11):
                base_no=base_convertor(num,j)
                #print 'j='+str(j)+'  '+str(base_no)
                cp=check_prime(base_no)
                
                if cp==0:
                    
                    temp.append(base_no)
                else:
                    f=1
                    break
        else:
            f=1

        if f==1:
            
            remove_list.append(num)
        else:
            count+=1
            possible.append(num)
            interpretation.append(temp)


dec_to_bin(n1)

#for i in range(len(possible_num)):
 #   possible_num[i]=int('1'+possible_num[i]+'1')
    
#print possible_num



divisor=[]
for i in interpretation:
    temp=[]
    for j in range(len(i)):
        #temp.append(divisorGen(i[j]))
        temp.append(factors(i[j]))
    divisor.append(temp)


for i in range(len(divisor)):
    divisor[i]=(' '.join(map(str, divisor[i])))

inf.close()
outf=open('C:\\Users\\Anchit\\Downloads\\code jam\\test_output.txt','w')
outf.write('Case #1:\n')
for i in range(m):
    outf.write(str(possible[i])+' '+divisor[i]+'\n') 
outf.close()
        
