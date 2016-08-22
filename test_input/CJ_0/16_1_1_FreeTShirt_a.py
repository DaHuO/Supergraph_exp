def argmax(s):
    z = max(s)
    return [(idx, c) for idx, c in enumerate(s) if c == z]

def last(s):
    if len(s) <= 1:
        return s
    return max([s[idx]+last(s[:idx])+s[idx+1:] for idx, c in argmax(s)])

fw = open('a-o', 'w')
for idx, line in enumerate(open('A-small-i')):
    if idx == 0:
        continue
    s = line.strip()
    print(s)
    fw.write('Case #{0}: {1}\n'.format(idx,last(s)))
