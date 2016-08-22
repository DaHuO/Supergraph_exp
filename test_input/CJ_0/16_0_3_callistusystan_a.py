def intput():
    return int(input())
def insplit():
    return input().split()
def intsplit():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a
def strtolist(a):
    list = []
    for c in a:
        list.append(c)
    return list
def s(a):
    return str(a)

def check_jam(a):
    if a[0] != "1" or a[-1] != 1:
        return False

def check_prime(n):
    if n%2==0:
        return False
    else:
        i = 3
        while i*i <=n:
            if n%i==0:
                return False
            i+=2
        return True

def get_K(n):
    for i in range(2,n-1):
        if n%i == 0:
            return i
        

T = intput()
for t in range(T):
    line = intsplit()
    print("Case #" + str(t+1) + ": ")
    N = line[0]
    J = line[1]

    n = 0
    for i in range(2**(N-1)+1,2**N,2):
        if n == J:
            break
        possible_jam = bin(i)[2:]
        valid = True
        for j in range(2,11):
            valueInJ = int(possible_jam,j)
            if check_prime(valueInJ):
                valid = False
                break
        if valid:
            print(possible_jam, end = "")
            for j in range(2,11):
                valueInJ = int(possible_jam,j)
                K = get_K(valueInJ)
                print("",K, end="")
            print()
            n+=1
            
        
