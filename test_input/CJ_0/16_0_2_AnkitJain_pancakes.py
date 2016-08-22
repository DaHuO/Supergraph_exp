
def flip(s, end):
    for i in range(0, end):
        if s[i] == '+':
            s[i] = '-'
        else:
            s[i] = '+'
    return s

def get_no_flips(s):
    s = [i for i in s]

    if '-' not in s:
        return 0

    if '+' not in s:
        return 1

    count = 1
    while True:
        end = len(s)
        for i in range(1, end):
            if s[i-1] != s[i]:
                end = i
                break

        s = flip(s, end)
        if '-' not in s:
            return count

        count += 1


T = int(raw_input())

for i in range(T):
    s = raw_input()
    print "Case #%s: %s" % (str(i+1), str(get_no_flips(s)))