fi = open('in', 'r')
fo = open('out', 'w')

T = int(fi.readline())
for t in range(T):
    s = str(fi.readline())
    ans = ''
    for si in s:
        if ans == '' or si < ans[0]:
            ans += si
        else:
            ans = si + ans

    fo.write('Case #{}: {}'.format(t + 1, ans))
