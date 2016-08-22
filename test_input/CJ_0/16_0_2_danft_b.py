import sys;
t=int(input());

for tt in range(0,t):
    sys.stdout.write('Case #{}: '.format(tt+1));

    s=input();

    ans=0;
    n=len(s);
    prv='x';
    for x in s:
        if(x!=prv and x=='-'): 
            ans+=1+(prv=='+');
        prv=x;
    print(ans);

    
