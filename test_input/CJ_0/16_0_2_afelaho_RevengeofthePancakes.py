def RevengeofthePancakes():
    f = open('B-large.in')
    f2 = open('B-large.out','w+')
    T = int(f.readline())

    for m in range(1, T+1):
        N = str(f.readline())
#        N = "---+"
        a = []
        l = 0
        i = 0
        j = 0
        for i in N:
            a.append(i)
        del a[-1]
        
        for j in range(len(a)-1):
            k=j+1
            if  a[j] != a[k]: l += 1
        if a[-1] == "-": l += 1
        print >>f2, "Case #"+str(m)+": "+str(l)

def main():
    RevengeofthePancakes()
    
main()

