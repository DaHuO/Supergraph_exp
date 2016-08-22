import sys
sys.setrecursionlimit(2000)

def find_greatest_char(s):
    chars = [c for c in s]
    chars.sort()
    max_char = chars[-1]
    return s.rfind(max_char)

def handle(s):
    if not s:
        return ''
    pivot = find_greatest_char(s)
    return s[pivot] + handle(s[0:pivot]) + s[pivot+1:]

import itertools

test_case = 'large'

# BASIC SETUP
import cStringIO

with open('{0}.in'.format(test_case)) as f:
    lines = f.readlines()
cases = int(lines.pop(0))

output = cStringIO.StringIO()
# END BASIC SETUP

for case in xrange(cases):
    s = handle(lines[case].strip())

    output_line = "Case #{0}: {1}".format(case+1, s)
    print output_line
    print >>output, output_line


### DEFAULT OUTPUT
with open('{0}.out'.format(test_case), 'w') as f:
    f.write(output.getvalue())
### DEFAULT OUTPUT
