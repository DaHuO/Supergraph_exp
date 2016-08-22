from math import pow


def find(s):
    out_str = s[0]
    for char in s[1:]:
        if char >= out_str[0]:
            out_str = char + out_str
        else:
            out_str += char
    return out_str

if __name__ == "__main__":
    import fileinput
    f = fileinput.input("D:/A-small-attempt0.in")

    T = int(f.readline())
    for case in xrange(1, T+1):
        s = f.readline()
        res = find(s)
        print "Case #{}: {}".format(case, res)

    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    # t = int(raw_input())  # read a line with a single integer
    # for i in xrange(1, t + 1):
    #     s = raw_input()  # read a list of integers, 2 in this case
    #     res = find(s)
    #     print "Case #{}: {}".format(i, res)

