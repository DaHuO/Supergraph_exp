
dataInput=open('C:\Users\AmrEzzat\Desktop\B-small-attempt1.in')
dataOutput=open('C:\Users\AmrEzzat\Desktop\B-small-attempt1.out','wb')
t = int(dataInput.readline())  # read a line with a single integer
for i in xrange(1, t + 1):
    cakes=dataInput.readline()
    for j in range(100):
        lastCakeOnBack=cakes.rfind('-')
        if lastCakeOnBack==-1: 
            print "Case #{}: {}".format(i, j)
            dataOutput.write("Case #{}: {}".format(i, j)+"\n")
            break
        else:
            plusOccToChange=0
            minusOccToChange=0
            for k in range(lastCakeOnBack+1):
                if cakes[k]=='+': plusOccToChange+=1
                if cakes[k]=='-': minusOccToChange+=1
            cakes=cakes.replace('+','*',plusOccToChange)
            cakes=cakes.replace('-','+',minusOccToChange)
            cakes=cakes.replace('*','-')
            