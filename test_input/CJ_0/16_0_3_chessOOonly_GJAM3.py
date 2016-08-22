#AUTHOR:PUNIT PATEL
def is_prime(n):
  if n==2 or n==3:
    return 0
  for k in range(2,int(n**0.5)+1):
    if n%k==0:
      #print str(n)+"@"+str(k)
      return k
  return 0

test_case=int(raw_input())
tm=1
while(tm<=test_case):
    #n,j=raw_input().split()
    #n=int(n)
    #j=int(j)
    n=16
    j=50
    jcount=0
    count=0
    number=32769
    binary=[]
    print "Case #"+str(tm)+": "
    while(jcount<j):
        a=[0]*11
        binary=bin(number)[2:]
        count=0
        #print len(binary)
        for i in range(2,11):
            integer=0
            for jj in range(len(binary)):
                if binary[jj]=='1':
                    integer+=i**(len(binary)-1-jj)
            temp=is_prime(integer)
            if(temp!=0):
                a[i]=temp 
        for k in range(len(a)):
            if(a[k]!=0):
                count+=1
        if(count==9):
            print binary,a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10]
            jcount+=1
        number+=2
    tm+=1
