
def find_last( l, c):
    llen = len(l)-1
    for i in xrange(llen, -1, -1 ):
        if l[i] == c:
            return i
    return -1

def fix_stack( pk_list ):
    flips_count = 0
    while '-' in pk_list:
        lastidx = find_last(pk_list,'-')
        for i in xrange(0, lastidx+1):
            pk_list[i] = '+' if pk_list[i] =='-' else '-'
        flips_count+=1
    return flips_count


T=int(raw_input())
for i in xrange(T):
    print("Case #%d: %d"%(i+1,fix_stack(list(raw_input()))))
