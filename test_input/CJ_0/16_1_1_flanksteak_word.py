import sys

def do_test_case(fd):
    tokens = fd.readline()

    line = tokens.strip()
    highest = 0
    word = ''

    for c in line:

        val = ord(c)

        if not word:
            word = c
            highest = val
            continue


        if highest > val:
            word += c
        else:
            highest = val
            word = c+word
        
    print word


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    sys.stdout.write("Case #%d: " % (i))
    do_test_case(fd)

