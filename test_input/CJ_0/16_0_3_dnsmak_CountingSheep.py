import itertools, math

def properdivisors1(n):
    pd=[]
    sum=1
    p=2
    j=0
    while(p*p<=n and n>1):
        if (n%p==0):
            j=p*p;
            n=n/p;
            #print n
            if (n!=1):
                pd.append(int(n))
            while(n%p==0):
                j=j*p;
                n=n/p;
                #print n
                if (n!=1):
                    pd.append(int(n))
            #sum=sum*(j-1);
            #sum=sum/(p-1);
        
        if (p==2):
            p=3;
        else:
            p=p+2;
    
    #if (n>1):
    #    sum=sum*(n+1);
    #print n,sum
    pd.sort()
    #print pd
    return pd[len(pd)/2]
    #return pd;



def properdivisors(n):
    pd=[]
    r= 1
    #sum =1
    f=0
    step=0;
    if(n==1):
        return 0;
    else:
        r=int(math.floor(math.sqrt(n)))
    
    #//first take into account the case that n is a perfect square.
    #print "r = ",r
    #pd.append(1)
    if (r*r==n): 
        #sum=1+r;
        pd.append(r)
        r=r-1;
    #else:
    #    sum=1;
    
    if (n%2==1):
        f=3;
        pd.append(3)
        step=2;
    else:
        f=2;
        pd.append(2)
        step=1;
    
    while (f<=r):
        if (n%f==0):
            pd.append(int(f))
            pd.append(int(n/f))
            #sum=(sum+f+n/f);
        
        f=f+step;
    pd1 = list(set(pd))
    pd1.sort()
    #print pd1,len(pd1),pd1[len(pd1)/2]
    return pd1[len(pd1)/2]
    #return pd1
    #return sum;

    

#print properdivisors1(220)

def isPrime(n):
    if(n==1):
        return False;
    elif (n<4):
        return True; #//2 and 3 are prime
    elif (n%2==0):
        return False;
    elif (n<9):
        return True; #//we have already excluded 4,6 and 8.
    elif (n%3==0):
        return False;
    else:
        r=math.floor(math.sqrt(n)); #// n rounded to the greatest integer r so that r*r<=n
        f=5;
        while(f<=r):
            if (n%f==0):
                return False; #// (and step out of the function)
            if (n %(f+2)==0): 
                return False; #//(and step out of the function)
            f=f+6;
    return True; #//(in all other cases)


def CoinJam(n,jv):
    res= {};
    it= list(itertools.product((0,1), repeat=n))
    for ite in it:
        if (ite[0]==1 and ite[-1]==1):
            totl = [];
            found=True
            for i in range(2,11):
                #print i,ite,ite[0],ite[-1],list(ite), ite[::-1]
                toti=0
                for ie,j in enumerate(ite[::-1]):
                    if (j==1):
                        toti+=math.pow(i,ie)
                        #print " " ,ie, j, math.pow(i,ie),toti,isPrime(toti)
                if (isPrime(toti)):
                    found=False
                    break;
                totl.append(properdivisors1(toti))
                #print toti, properdivisors1(toti)
                #print toti
                #properdivisors1(int(toti))
            if (found):
            #    print ite
                s=''
                for itev in ite:
                    s+=str(itev)
                res[s]=totl
                if (len(res)==jv):
                    return res
                #print len(res)
    #print res
    return res
        
            
def MainCoinJam():
    print "start"
    in_file = open('C:\\Users\\mkader\\downloads\\C-small-attempt1.in', 'r')
    ou_file = open('C:\\Users\\mkader\\downloads\\coinjam_out.txt', 'w')

    case = 1;
    in_file.readline();
    for in_data in in_file:
        ldata = in_data.strip(' \t\n\r')
        if(len(ldata)==0):
            break;
        else:
            in_line2 = (in_data.strip(' \t\n\r')).split()
            N = int(in_line2[0])
            J = int(in_line2[1])
            #print N, J
            d= CoinJam(N, J)
            #print d
            #print d.keys()
            print>>ou_file,'Case #'+str(case)+':'
            for dkv in d.keys():
                sdvv=''
                for dvv in d[dkv]:
                    sdvv+=' '+str(dvv)
                print>>ou_file, dkv+sdvv
 
    ou_file.close()
    print "done"

MainCoinJam()

def CountingSheep(n):
    digits = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    total=0;
    k=1;
    if n==0:
        return "INSOMNIA";
    else:
        while (True):
            for i in str(n*k):
                digits[i]=1;
                #print "i = " +i;
            if not (0 in digits.values()):
                return n*k;
            k+=1;
            #print k,n, " = ", digits, 0 in digits.values(), digits.values();
        

##if __name__ == "__main__":
##	testcases = input()
##	 
##	for caseNr in xrange(1, testcases+1):
##		cipher = raw_input()
##		print("Case #%i: %s" % (caseNr, solve(cipher)))

def MainCountingSheep():
    in_file = open('C:\\Users\\mkader\\downloads\\A-large.in', 'r')
    ou_file = open('C:\\Users\\mkader\\downloads\\google_test_out.txt', 'w')

    case = 1;
    in_file.readline();
    for in_data in in_file:
        ldata = in_data.strip(' \t\n\r')
        if(len(ldata)==0):
            break;
        else:
            #print ldata,CountingSheep(int(ldata))  ;  
            print>>ou_file,'Case #'+str(case)+': '+str(CountingSheep(int(ldata)));
            case+=1;
    ou_file.close()

##print CountingSheep(0);
##print CountingSheep(1);
##print CountingSheep(2);
##print CountingSheep(11);
##print CountingSheep(1692);
