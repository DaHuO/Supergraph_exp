import sys

def count_flips(S):
    ret = 0
    S = compress(S)
    j = len(S)
    i = 0
    while (j > i):
        # print S[i:j]
        ret += 1
        if S[i] == '-':
            i += 1
        else:
            if (j - i) == 1:
                break
            i += 1
    return ret

def compress(S):
    ret = []
    for i in xrange(len(S)):
        if i == 0:
            ret.append(S[i])
        else:
            if S[i] != S[i-1]:
                ret.append(S[i])
    if ret[-1] == '+':
        ret = ret[:-1]
    return "".join(ret)

if __name__ == "__main__":
    output_file = open("%s.%s" % (sys.argv[1].split(".")[0], "out"), "w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        pancakes = input_file.readline().strip()
        # print pancakes
        result = count_flips(pancakes)
        output_file.write("Case #%s: %s\n" % (i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
