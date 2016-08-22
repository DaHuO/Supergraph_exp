def is_prime(n):
    if(n == 2 or n == 3): 
        return True
    if(n < 2 or n%2 == 0): 
        return False
    if(n < 9): 
        return True
    if(n%3 == 0): 
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        # print '\t',f
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True   



n = 16
numOut = 50

bits = [0]*n
bits[0] = 1
bits[-2] = -1
bits[-1] = 1
#print(bits)

diffBits = pow(2,n-2);
for i in range(diffBits):
    bits[n-2]+=1
    for j in range(n-2,-1,-1):
        if(bits[j] == 2):
            bits[j] = 0;
            bits[j-1]+=1
    bitStr = "".join(str(x) for x in bits)
    #print(bitStr)
    bases = []
    ill = False
    for j in range(2,11):
        bases.append(int(bitStr,j))
        if(is_prime(bases[-1])):
            ill = True
            break
    #print(bases)
    if(not ill):
        numOut-=1
        print(bitStr, end="")
        
        for j in range(9):
            for k in range(2,bases[j]):
                if(bases[j]%k == 0):
                    print(" ",k, end="")
                    break
                    
        
        if(numOut!=0):
            print()
        else:
            print()
            break
