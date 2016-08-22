#!/usr/bin/python

def parse():
    return raw_input()

def solve(S):
    result = ""
    for letter in S:
        result = max(result+letter, letter+result)
    return result

def main():
    for i in range(int(raw_input())):
        S = parse()
        result = solve(S)
        print 'Case #%s: %s' % (i+1, result)

if __name__ == "__main__":
    main()
