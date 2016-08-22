import sys
sys.setrecursionlimit(10000)

def last_word(s, res):
    if s == '':
        return res
    if res == '':
        return last_word(s[1:], s[0])
    if s[0] >= res[0]:
        return last_word(s[1:], s[0] + res)
    return last_word(s[1:], res + s[0])

for t in range(int(input())):
    s = input()
    print("Case #{0}: {1}".format(t+1, last_word(s, '')))
