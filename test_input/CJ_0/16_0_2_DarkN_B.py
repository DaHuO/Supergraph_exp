import sys

if __name__ == "__main__":
    _in = open("B.in", "r")
    _out = open("B.out", "w")
    T = int(_in.readline())
    for i in range(T):
        line = _in.readline()[:-1]
        while ((len(line)>0) and (line[-1] == '+')):
            line = line[:-1]
        count = 0
        if (len(line) != 0):
            c = line[0]
            index = 1
            while (index < len(line)):
                if (c != line[index]):
                    c = line[index]
                    count += 1
                index += 1
            count += 1
        _out.write("Case #" + str(i+1) + ": " + str(count)+"\n")
