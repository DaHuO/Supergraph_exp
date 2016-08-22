import math as m

f = open("A-large.in", 'r') #opens a file at the beginning
line=f.readline() #reads the next line of the file (until next \n)
N=int(line)
for i in range(N):
    line=f.readline()
    line=line.split('\n')[0]
    s = line[0]
    firstchar = line[0]
    for char in line[1:]:
        if ord(char) >= ord(firstchar):
            s = char + s
            firstchar = char
        else:
            s += char
    print('Case #'+str(i+1)+': '+s)