import sys

def last_word(string):
    for char in [chr(i) for i in xrange(ord('Z'), ord('A') - 1, -1)]:
        count_char = string.count(char)
        if count_char == 0:
            continue
        return '%s%s%s' % (char * count_char,
                           last_word(string[:string.index(char)]),
                           string[string.index(char) + 1:].replace(char, ''))
    return ''

if __name__ == '__main__':
    with open(sys.argv[1]) as fd:
        lines = [line.strip() for line in fd.readlines()]
    for index, line in enumerate(lines[1:]):
        print 'Case #%d: %s' % (index + 1, last_word(line))
