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

def f(a,j):
    for i in range(j):
        if a[i] == "+":
            a[i] = "-"
        else:
            a[i] = "+"

T = intput()
for t in range(T):
    sidestr = input()

    nPancakes = len(sidestr)
    
    a = []

    for i in sidestr:
        a.append(i)
        
    i = 0
    while a != ["+"]*nPancakes:
        char = a[0]
        if char == "+":
            if "-" in a:
                j=a.index("-")
                f(a,j)
                i+=1
            else:
                break
        elif char == "-":
            if "+" in a:
                j=a.index("+")
                f(a,j)
                i+=1
            else:
                i+=1
                break
    
    
    
    print("Case #" + str(t+1) + ": " + str(i))
