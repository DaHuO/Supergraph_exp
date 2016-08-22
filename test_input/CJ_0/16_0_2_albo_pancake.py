#!/usr/bin/python

import sys, os
import readline

test_cases = None
test_case = None

def test_input(v):
    s = []
    for i in v:
        s.append(i)

    flip = 0

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            # everything is ok, do nothing
            None

        elif s[i] != s[i+1]:
            # flip case

            if s[i] == "-":
                flip += 1

                for j in range(0, i):
                    if s[j] == "-":
                        s[j] = "+"
                    else:
                        s[j] = "-"

            elif s[i] == "+":
                flip += 1

                for j in range(0, i):
                    if s[j] == "-":
                        s[j] = "+"
                    else:
                        s[j] = "-"

    if s[len(s)-1] == "-":
        flip += 1

    return ("%s" % (flip))

if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    while True:
        line = f.readline()
        if line == None or len(line) == 0:
            break

        if test_cases == None:
            test_cases = int(line)
            test_case = 0
            continue
        else:
            test_case += 1
            val = line.replace("\n", "").replace("\r", "")

        if test_case <= test_cases:
            print("Case #%i: %s" % (test_case, test_input(val)))
        else:
            break

    f.close()
        
    sys.exit(0)
