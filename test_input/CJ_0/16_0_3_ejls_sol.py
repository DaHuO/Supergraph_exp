from random import randint
n=16
j=50

def good(x):
    for d in range(2, min(x-1, 10000)):
        if x%d==0:
            return d
    return False

print('Case #1:')
found = []
for _ in range(j):
    while True:
        xs = '1' + ''.join(["01"[randint(0,1)] for _ in range(n-2)]) + '1'
        r = []
        for b in range(2, 11):
            x = int(xs, b)
            r.append(good(x))
            if r[-1]==False:
                break
        if r[-1]!=False and xs not in found:
            print(xs+' '+(' '.join(map(str, r))))
            found.append(xs)
            break
