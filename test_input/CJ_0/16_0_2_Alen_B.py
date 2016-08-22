#!/usr/bin/env python
# encoding: utf-8

def solve(line):
    t = 0
    pch = '+'
    for ch in line.strip()[::-1]:
        if ch != pch:
            t += 1
            pch = ch
    return t


def run(inputFile, outputFile):
    fp = open(inputFile, 'r')
    fw = open(outputFile, 'w')
    caseIndex = 0
    count = -1
    for line in fp:
        if (caseIndex == 0):
            count = int(line)
            caseIndex += 1
        else:
            fw.write("Case #%d: %d\n" % (caseIndex, solve(line)))
            caseIndex += 1
            count -= 1
        if (count == 0):
            break
    fp.close()
    fw.close()


if __name__ == "__main__":
    run("in", "out")