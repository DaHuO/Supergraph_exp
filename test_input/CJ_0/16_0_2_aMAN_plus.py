t = int(input())
arr = []
s = ""
times = 0
def rev(x): # index of last from 0
    global arr
    global times
    times = times +1
    half = (x+1)//2
    for i in range(half):
        temp = 1 - arr[i]
        arr[i] = 1 - arr[x-i]
        arr[x-i] = temp
    if((x+1)%2 != 0):
        arr[half] = 1 - arr[half]
        
def check(n):
    global arr
    for i in range(n-1):
        if(arr[i]!=arr[i+1]):
            return i

    return -1

def ini():
    global s
    global arr
    for i in range(len(s)):
        if(s[i] == '+'):
            arr.append(1)
        else:
            arr.append(0)
            
for i in range(t):
    global arr
    global s
    global times
    
    s = input()
    ini()
    boo = True
    while(boo):
        j = check(len(s))
        if(j== (-1)):
            boo = False
        else:
            rev(j) # index

        if(1 not in arr):
            rev(len(s)-1)

            boo = False
        elif(0 not in arr):
            boo = False
        
    #######################
    print("Case #"+str(i+1)+": "+str(times))
    arr = []
    s = ""
    times = 0
            
        
