#!/usr/bin/env python3

FILENAME = "A-large"


with open(FILENAME + ".in", 'r') as inputfile:
    lines = inputfile.readlines()

with open(FILENAME + ".out", 'w') as outputfile:
    number_of_tests = 0
    for linenumber, line in enumerate(lines):
        if linenumber == 0:
            number_of_tests = int(line.strip())
            print("There are {} tests".format(number_of_tests))
        elif linenumber > number_of_tests:
            break
        else:
            casenumber = linenumber
            
            S = line.strip()
            
            out=''
            for C in S:
                if not out:
                    out=C
                else:
                    if C < out[0]:
                        out = out + C
                    else:
                        out = C + out

            assert len(out) == len(S)
            answer = "Case #{}: {}\n".format(casenumber, out)
            print(answer)
            outputfile.write(answer)
