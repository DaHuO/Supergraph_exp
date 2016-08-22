def last_word(s):
    result = ''

    for c in s:
        if c + result > result:
            result = c + result
        else:
            result = result + c

    return result

def main():
    N = int(input())

    for t in range(1, N + 1):
        s = input().strip()
        print("Case #%d: %s" % (t, last_word(s)))

main()
