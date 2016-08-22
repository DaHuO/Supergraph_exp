t = int(raw_input())
for i in xrange(1, t + 1):
    #word = [str(w) for w in raw_input().split()]
    word = [c for c in str(raw_input())]
    list(word)
    last = str(word[0])
    
    length = len(word)
    

    first = word[0]
    for j in xrange(1, length):
        if word[j] < first:
            last += str(word[j])
        else:
            last = str(word[j]) + last
            first = last[:1]

    print "Case #{}: {}".format(i, last)
        
