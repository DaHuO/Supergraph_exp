import sys

def count_changes(seq):
    count = 0
    cur_char = seq[0]
    for ii in range(1, len(seq)):
        next_char = seq[ii]
        if cur_char != next_char:
            count += 1
        cur_char = next_char
    if cur_char == '-':
        count += 1
    return count

f = open(sys.argv[1])
T = int(f.readline())
for test in range(T):
    seq = f.readline().strip()

    print "Case #%d: " % (test + 1), count_changes(seq)
