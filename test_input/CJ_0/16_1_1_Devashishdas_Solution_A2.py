
def gene(word, last):
    return [word + last, last + word]




def generate(word):
    lis = []
    s = []
    if len(word) ==   1: return word
    for i in word[1:]:
        if len(lis) == 0:
            lis += gene(word[0], word[1])
            new = 0
        else:
            new = max([len(h) for h in lis]) + 1
            s = reduce(lambda x,y: x+y, [gene(j, i) for j in lis])
            lis = s
    lis.sort()
    return lis[-1]




test = int(raw_input())
for test_num in range(test):
    value = raw_input()
    print "Case #%d: %s"%((test_num+1), generate(value))
