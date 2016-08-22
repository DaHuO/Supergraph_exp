from flipper import do_flip

test_case = 'large'

# BASIC SETUP
import cStringIO

with open('{0}.in'.format(test_case)) as f:
    lines = f.readlines()
cases = int(lines.pop(0))

output = cStringIO.StringIO()
# END BASIC SETUP

for case in xrange(cases):
    stack = [c for c in lines[case].strip()]

    output_line = "Case #{0}: {1}".format(case+1, do_flip(stack))
    print output_line
    print >>output, output_line


### DEFAULT OUTPUT
with open('{0}.out'.format(test_case), 'w') as f:
    f.write(output.getvalue())
### DEFAULT OUTPUT
