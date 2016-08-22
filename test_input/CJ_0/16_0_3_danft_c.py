import sys;


def tobase(x, b):
    ret=0;
    for i in range(31,-1,-1):
        ret*=b;
        if(x & (1<<i)):
            ret+=1;
    return ret;


t=int(input());

for tt in range(0,t):

    n, k=input().split();
    n=int(n);
    k=int(k);


    #print(tobase(5, 9));
    x=1<<(n-1);
    x+=1;

    c=0;


    print("Case #1:");
    while c<k: 
        if(x >= 1<<n):
            break;
        ans="";
        ok=True;
        for b in range(2, 11):

            y=tobase(x, b);
             
            okk=False;
            for i in range(2, 1000):
                if(y%i==0 and i < y):
                    okk=True;
                    ans+=str(i) + " ";
                    break;
            if(okk==False):
                ok=False;
                break;
        if(ok):
            sys.stdout.write(bin(x)[2:]+" ");
            print(ans);
            c+=1;
        x+=2;
    #print(c);


