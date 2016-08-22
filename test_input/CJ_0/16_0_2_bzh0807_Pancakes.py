#Bill Zhang
#Pancakes
#Google Code Jam

def readFile():
    file = open('B-large.in', 'r')
    #file = open('pancakesample.txt', 'r')
    fileout = open('pancakeout.txt', 'w')
    num = int(file.readline())
    for n in range(num):
        x = file.readline()
        if n != num-1:
            fileout.write("Case #"+str(n+1)+": "+str(flips(x))+"\n")
        else:
            fileout.write("Case #"+str(n+1)+": "+str(flips(x)))

def flips(pancakes):
    elem = []    
    for i in pancakes:
        #print(i)        
        if i == '+':
            elem.append(1)
        elif i == '-':
            elem.append(-1)
    it = 0
    for k in range(len(elem)):
        x = elem[len(elem)-1-k]
        if x < 0:
            it += 1
            elem = [n*-1 for n in elem]
    return it

readFile()