
def solve(s: str) -> str:
    ret = s[0]
    for ch in s[1:]:
        if ch >= ret[0]:
            ret = ch + ret
        else:
            ret = ret + ch
    return ret

if __name__ == '__main__':

    lines_count = int(input())

    words = []
    for i in range(lines_count):
        words.append(input())

    for i in range(lines_count):
        ret = solve(words[i])
        print('Case #%d: %s' % (i+1, ret))
