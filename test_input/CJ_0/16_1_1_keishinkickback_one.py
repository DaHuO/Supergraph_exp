import fileinput
import collections

def compute(line):
    newline = [line[0]]
    for ch in line[1:]:
        if ch >= newline[0]:
            newline.insert(0,ch)
        else:
            newline.append(ch)
    return ''.join(newline)

if __name__ == "__main__":
    f = fileinput.input()
    #test
    #f = open('sample.in','r')

    T=int(f.readline())
    for line in range(1,T+1):
         print("Case #{0}: {1}".format(line, compute(f.readline().split()[0])))

