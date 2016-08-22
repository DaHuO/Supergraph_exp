import sys
import math
sys.setrecursionlimit(10000)

T = int(raw_input())

for _test in range(1, T + 1):
    answer = ""

    S = raw_input()

    for c in S:
        #print answer
        if answer == "":
            answer += c
        else:
            #print answer[0], ">", c
            if answer[0] > c:
                answer += c
            else:
                answer = c + answer

    print "Case #{}: {}".format(_test, answer)

