t = int(raw_input())
for x in xrange(1,t+1):
    string = list(raw_input())
    result = [string[0]]
    for letter in string[1:]:
        if letter >= result[0]:
            result = [letter] + result
        else:
            result = result + [letter]
    print "Case #{}: {}".format(x, ''.join(result))
