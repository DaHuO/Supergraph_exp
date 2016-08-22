###AUTHOR:PUNIT PATEL###
def is_prime(n):
  if n == 2: return 0
  if n == 3: return 0
  if n < 2: return 0
  if n%2 == 0: return 2
  if n < 9: return 0
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    #print '\t',f
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f +=6
  return 0


test_case=int(raw_input())
tm=1
while(tm<=test_case):
    n,j=raw_input().split()
    n=int(n)
    j=int(j)
    jcount=0
    count=0
    number=2**31+1
    binary=""
    print "Case #"+str(tm)+": "
    while(jcount<j):
        a=[0]*11
        binary=bin(number)[2:]
        count=0
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
