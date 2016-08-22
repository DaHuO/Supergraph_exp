file = open("/Users/cdong/Dropbox/cdong-ltm1/GitRepo/CodeJam2016/A-large.in")
no_test = int(file.readline())


def get_output(s):
    l = []
    first = None
    for i in s.strip():
        if first:
            if i < first:
                l.append(i)
            else:
                l.insert(0, i)
                first = i
        else:
            l.append(i)
            first = i

    return "".join(l)


for i in range(0, no_test):
    print("Case #%s: %s" % (i + 1, get_output(file.readline())))
