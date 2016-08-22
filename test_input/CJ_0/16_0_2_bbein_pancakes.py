def convert(s):
    l = []
    for char in s:
        if char == "+":
            l.append(True)
        else:
            l.append(False)
    return l

def flip(l):
    l.reverse()
    for i,x in enumerate(l):
        if x:
            l[i]=False
        else:
            l[i]=True
            
def check_numbers(numbers):
    for x in numbers:
        if not x:
            return False
    return True

def remove(l):
    i = len(l)-1
    while(l[i]):
        l.pop()
        i-=1
        if i < 0:
            break

f = open("B-large.in", 'r') #opens a file at the beginning
line=f.readline() #reads the next line of the file (until next \n)
N=int(line)
for i in range(N):
    N2 = 0
    line=f.readline()
    line = line.split(sep='\n')[0]
    pancake = convert(line)
    if pancake:
        remove(pancake)
    while pancake:
        if pancake[0]:
            j=1
            while pancake[j]:
                j+=1
            N2+=1
            temp = pancake[:j]
            flip(temp)
            for k in range(j):
                pancake[k] = temp[k]
        N2+=1
        flip(pancake)
        remove(pancake)
    print('Case #'+str(i+1)+': '+str(N2))