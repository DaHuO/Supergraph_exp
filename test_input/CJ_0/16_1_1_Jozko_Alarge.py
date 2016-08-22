import sys
import numpy as np
T = int(sys.stdin.readline())
for case in range(1, T+1):
    sys.stdout.write("Case #%d: " % case)
    word = sys.stdin.readline().strip()

    states = set([""])

    last_word = word[0]
    for c in word[1:]:
        if c < last_word[0]:
            last_word = last_word + c
        else:
            last_word = c + last_word
    sys.stdout.write("%s\n" % last_word)

