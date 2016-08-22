with open("input.txt","r+") as f:
    n = int(f.readline())
    w = open("output.txt","w")
    for a0 in range(1,n+1):
        s = f.readline()
        count = 0
        l = len(s)-1
        i = 0
        flag = 0
        while(s[i] != "\n"):
            r = 0
            while(s[i] == '-' and i<l):
                #print s[i],
                r+=1
                i+=1
                
            if r>0:
                count+=1
            while(s[i] == '+' and i<l):
                #print s[i],
                i+=1
                
        if(s[0] == '-'):
            sw = "Case #%d: %d\n"%(a0,(count*2)-1)
            print sw
            w.write(sw)
        else:
            sw = "Case #%d: %d\n"%(a0,count*2)
            print sw
            w.write(sw)
        
w.close()
