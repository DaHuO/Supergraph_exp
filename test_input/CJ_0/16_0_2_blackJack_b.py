c = int(raw_input())

def swap(s):
    return ''.join(['-' if c == '+' else '+' for c in s])

def turns(s, hashmap):
    if s in hashmap:
        return hashmap[s]
    for i in reversed(range(len(s))):
        if s[i] != s[-1]:
            break
    split_s = s[:(i+1)]
    if s[-1] == '+':
        result = turns(split_s, hashmap)
    else:
        result = 1 + turns(swap(split_s), hashmap)
    hashmap[s] = result
    return result

for idx in range(c):
    s = raw_input()
    hashmap = {'': 0, '+': 0}
    print "Case #{0}: {1}".format(idx+1, turns(s, hashmap))
