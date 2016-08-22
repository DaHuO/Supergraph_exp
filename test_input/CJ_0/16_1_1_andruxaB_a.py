filename = "/home/andybozhko/Downloads/python/codejam/Round 1A/A/A-large"

fin = open(filename+".in")
fout = open(filename+".out","w")

trials = int(fin.readline())

for T in xrange(trials):
    
    string = fin.readline().strip()
    
    myword = string[0]
    
    for c in string[1:]:
        s1 = myword + c
        s2 = c + myword
        if s1 > s2:
            myword = s1
        else:
            myword = s2
    
    fout.write("Case #{0}: {1}\n".format(T+1, myword))
                    
fin.close()
fout.close()