def flip(s, i):
    for j in range(0, i+1):
        if s[j]=="-":
            s = s[:j] + "+" + s[j+1:]
        else:
            s = s[:j] + "-" + s[j+1:]
    return s
    
def check(s):
    for i in range(len(s)-1,-1,-1):
        if s[i]!="+":
            return False, i
    return True, -1
        
def calculate(pan):
    count = 0
    for i in range(1, 101):
        cake = pan
        a,b = check(cake)
        if a==False:
            #print (cake)
            cake = flip(cake, b)
            #print (cake)
            count = count + 1
            pan = cake
        else:
            return count
    
t = int(input())       
for i in range(1, t + 1):
    pancake = input()
    print("Case #{}: {}".format(i, calculate(pancake)))