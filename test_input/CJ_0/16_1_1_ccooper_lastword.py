import sys

lines = sys.stdin.readlines()

test_cases = int(lines[0].strip())

for test_case in range(1, test_cases + 1):
    letters_in = lines[test_case].strip()

    letters_out = letters_in[0]
    for letter in letters_in[1:]:
        if letter < letters_out[0]:
            letters_out = '%s%c' % (letters_out, letter)           
        else:
            letters_out = '%c%s' % (letter, letters_out)

    print 'Case #%d: %s' % (test_case, letters_out)