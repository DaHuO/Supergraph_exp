t = int(raw_input())
for i in xrange(1, t + 1):
    pancakes = str(raw_input())
    length = len(pancakes)
    counter = 0
    
    if length > 1:
        for x in xrange(0, length - 1):
            if pancakes[x] != pancakes[x + 1]:
                counter += 1
                
    if pancakes[length - 1] == '-':
        counter += 1
    
    print "Case #{}: {}".format(i, counter)
        