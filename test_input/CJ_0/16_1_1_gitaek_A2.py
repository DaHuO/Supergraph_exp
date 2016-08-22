import sys

#fi = open(sys.argv[1], 'r')
#fo = open(sys.argv[2], 'w')

finam = 'A-large.in'
fonam = 'A-large.out'
#finam = 'A-small-attempt0.in'
#fonam = 'A-small.out'
fi = open(finam)
fo = open(fonam, 'w')
T = int(fi.readline())

for t in range(T):
    S = fi.readline().strip().split(' ')[0]
    P = ''
    for s in S:
        if P == '':
            P = s
        else:
            if s >= P[0]:
                P = s + P
            else:
                P = P + s
    print S, P
    sol = 'Case #'+str(t+1)+': '+P
    #print sol            
    fo.write(sol+'\n')
fi.close()
fo.close()

        
