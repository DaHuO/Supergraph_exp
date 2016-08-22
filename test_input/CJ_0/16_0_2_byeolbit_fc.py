f = open("B-large.in.txt",'r')
A = open("b.output.txt",'w')

C = f.readline()
for c in xrange(0,int(C)):
    fl = [False if s is '-' else True for s in f.readline()]
    fl.pop()
    count = 0
    state = False

    n=0;

    for i in fl:
        if n+1 is len(fl) : break

        if i is not fl[n+1]:
            #import pdb;pdb.set_trace()
            if n is 0:
                fl[0] = not fl[0]
                count+=1
                #print fl
                #print "a"
            else:
                for j in range(0,n):
                    fl[j] = not fl[j]
                count+=1
                #print fl
                #print "b"
        n+=1
    if fl[0] is False :
        #print "check!"
        count+=1

    answer = 'Case #{0}: {1}'.format(c+1, count)
    print answer
    A.write(answer+'\n')
f.close
A.close
