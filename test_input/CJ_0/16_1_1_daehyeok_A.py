import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def solve(n):
    if len(n) < 2:
        return n
    re = n[0]
    for ch in n[1:]:
        if ord(ch) < ord(re[0]):
            re += ch
        else:
            re = ch + re
    return re

def main():
    t = int(input())

    for i in range(t):
        #list(map(int, input().split()))
        n = input()
        print("Case #%d: " % (i + 1)  , end="")
        print(solve(n))

def log(*message):
    logging.debug(*message)
    
if __name__ == "__main__":
    main()
