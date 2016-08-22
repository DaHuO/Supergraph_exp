from math import factorial as fff
from fractions import gcd 
f=pow(2,3,3)
xs=fff(f+2)
author='biggy_bs'
# Main code goes here !!
t=input()
case=1
dp=[0]*110
while t>0:
    t-=1
    dp=[0]*110
    ct=0
    s=raw_input()
    n=len(s)
    arr=list(s)
    for i in range(n,0,-1):
        if arr[i-1]=='-':
            if dp[i+1]&1:
                dp[i]=dp[i+1]
            else:
                dp[i]=dp[i+1]+1
        else:
            if dp[i+1]&1:
                dp[i]=dp[i+1]+1
            else:
                dp[i]=dp[i+1]
    print 'Case #'+str(case)+': '+str(dp[1])
    #print 'Case #'+str(case)+': '+str(ct)
    case+=1
