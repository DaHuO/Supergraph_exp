f = open("A-large (1).in",'r')
f2 = open("A-large (1).out","w")
f.readline()
num = 1
for line in f:
    
    lastword = ""
    for char in line:
        if len(lastword)==0:
            lastword += char
        else:
            if char >= lastword[0]:
                lastword = char + lastword
            else:
                lastword+=char
    f2.write("Case #{0}: {1}".format(num,lastword))
    num+=1