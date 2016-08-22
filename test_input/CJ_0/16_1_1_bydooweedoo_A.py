import sys

def getLines():
    return [line.rstrip('\n') for line in sys.stdin]

def solve(chars):
    word = chars[0]
    for index in range(1, len(chars)):
        char = chars[index]
        if ord(char) >= ord(word[0]):
            word = char + word
        else:
            word += char
    return word

lines = getLines()
nbCases = int(lines.pop(0))

for case in range(0, nbCases):
    chars = lines.pop(0).strip()
    answer = solve(chars)
    print("Case #", (case + 1), ": ", answer, sep="")
