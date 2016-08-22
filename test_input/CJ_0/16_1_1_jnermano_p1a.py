for t in range(input()):
    s = raw_input()
    ret = s[0]
    
    for x in s[1:]:
        if x < ret[0]:
            ret += x
        else:
            ret = x + ret
    print "Case #{}: {}".format(t+1, ret)
        
