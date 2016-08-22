import sys
import math
import itertools
import string

def main(infile, outfile):

    with open(infile) as inf:
        with open(outfile, 'w') as outf:
            test_case = 1
            t = int(inf.readline())
            for line in inf.readlines():

                bstr = line[0]
                line =  line.replace('\n', '')[1:]
                for char in line:
                    if char >= bstr[0]:
                        bstr = char + bstr
                    else:
                        bstr = bstr + char

                outf.write("Case #{}: {}".format(test_case, bstr))

                if t != test_case:
                    outf.write('\n')

                test_case += 1


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    main(infile, outfile)
