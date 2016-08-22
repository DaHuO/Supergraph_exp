def flip_str(s):
    return s.replace('+', '!').replace('-', '+').replace('!', '-')


def get_min_flip(s):
    l = len(s)
    correct_str = '+' * l
    count = 0    
    i = 0
    while correct_str != s:
        if s[l-i-1] == '-':
            s = flip_str(s[:l-i]) + s[l-i:]
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    t = int(input())
    l = list()
    for i in range(t):
        l.append(str(raw_input()))
    for i in range(1, t+1):
        n = get_min_flip(l[i-1])
        print "Case #{}: {}".format(i, n)

