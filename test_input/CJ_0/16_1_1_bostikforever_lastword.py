import sys


def last_word(S):
    ret = []
    for i in S:
        if ret and i >= ret[0]:
            ret.insert(0, i)
        else:
            ret.append(i)
    return "".join(ret)


if __name__ == "__main__":
    output_file = open("%s.%s" % (sys.argv[1].split(".")[0], "out"), "w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        ret = input_file.readline().strip()
        # print pancakes
        result = last_word(ret)
        output_file.write("Case #%s: %s\n" % (i+1, result))

    output_file.close()
    input_file.close()
    print "Done!"
