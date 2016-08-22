f1 = open("input4.in","r")
f2 = open("output4.in","w")

T = int(f1.readline())
#print T

for i in xrange(T):

    s = f1.readline()
    arr = list(s)

    try:
        arr.remove("\n")

    except:
        pass
    
    #print arr

    count = 0

    j = len(arr)-1

    k = 1

    while j >= 0:

        if k %2 !=0:
            l = j
            while l >=0 and arr[l] == "-":
                l -= 1

            if l != j:
                count += 1
                k += 1
                j = l

            else:
                j -= 1

        elif k%2 == 0:
            while arr[j] == "+":
                j -= 1

            count += 1
            k += 1

    f2.write("Case #"+str(i+1)+": "+str(count)+"\n")
    #print "count:",count

f1.close()
f2.close()
            
        
