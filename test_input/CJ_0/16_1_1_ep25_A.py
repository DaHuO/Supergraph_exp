import sys

def findLastWord(inStr):
    firstChar = inStr[0]
    lastWord = [firstChar]
    for c in inStr[1::]:
        test = firstChar > c
        # print("C={0}, f={1}, test={2}".format(c, firstChar, test))
        if test:
            # Insert at the end
            lastWord.append(c)
        else:
            # Insert at the beginning
            lastWord.insert(0, c)
            firstChar = lastWord[0]
    assert len(inStr) == len(lastWord)
    return "".join(lastWord)

def main():
    ln = 0
    T = None
    for line in sys.stdin:
        if ln == 0:
            T = int(line)
            ln += 1
        else:
            inStr = line.rstrip()
            sol = findLastWord(inStr)
            print("Case #{0}: {1}".format(ln, "".join(sol)))
            ln += 1

if __name__ == '__main__':
    main()