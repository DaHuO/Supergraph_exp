import sys

sys.stdout = open("./ans.out", 'w')

def theLastWord(str):
    array_str = list(str)
    return reduce(getBiggerWord, array_str)

def getBiggerWord(word, letter):
    if letter+word < word+letter:
        return word+letter
    else:
        return letter+word

with open('input.in') as inp:
    for idx, line in enumerate(inp):
        if not idx:
            continue
        print "Case #%d: %s"  %(idx, theLastWord(line))
