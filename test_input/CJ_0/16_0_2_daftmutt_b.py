import sys

fi = open('B-large.in', 'r')
fo = open('b.out', 'w')

T = int(fi.readline())
    
for i in xrange(T):
    # solve
    pancakes = fi.readline()
    
    prev = pancakes[0]
    
    flips = 0 if prev == '+' else 1
    
    for p in pancakes[1:]:
        if p != prev:
            if p == '-':
                flips += 2
            
        prev = p
    
    fo.write('Case #{}: {}\n'.format(i + 1, flips))
    print 'Case #{}: {}'.format(i + 1, flips)
    
fi.close()
fo.close()