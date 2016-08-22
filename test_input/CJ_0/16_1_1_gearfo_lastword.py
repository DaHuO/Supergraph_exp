from __future__ import division, print_function
import sys
import math

def maxindex(a_list):
    l = len(a_list)
    index = l-1
    char = a_list[-1]
    for j in range(l-1, -1, -1):
        if a_list[j] > char:
            char = a_list[j]
            index = j
    return index


def lastword(string):
    letters = [c for c in string]
    index = maxindex(letters)
    output = ""
    while index != 0:
        output += letters[index]
        letters = letters[:index] + letters[index+1:]
        index = maxindex(letters[:index])
    output += ''.join(letters)
    return output


def main():
    with sys.stdin as infile:
        test_cases = int(infile.next())
        for case in range(1, test_cases + 1):
            tc_data = infile.next().strip()
            result = lastword(tc_data)
            print("Case #%s: %s" % (case, result))
    pass

if __name__=="__main__":
    sys.exit(main())
