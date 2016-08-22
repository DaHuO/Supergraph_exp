#python 2.7

import sys
import math
import string


def solve(S):
    ret = ""
    for c in S:
        if (ret == ""):
            ret += c
        elif (ret[0] > c):
            ret = ret + c
        else :
            ret = c + ret
    return ret
    
def main():
    if (not len(sys.argv) == 3):
        print("Need exactly twos args: input filename and output filename")
        return
    input_data = open(sys.argv[1], 'r').read()
    output_file = open(sys.argv[2], 'w')
    split_input = input_data.split("\n")
    case_count = int(split_input[0])
    for i in range(0,case_count):
        res = solve(split_input[i+1])
        output_file.write("Case #" + str(i+1) + ": " + str(res) + "\n")
    
if __name__ == "__main__":
    main()
