import itertools
num_cases = int(raw_input())
for case in xrange(num_cases):
    stack = raw_input()
    if "-" not in stack:
        answer = 0
    else:
        grouped = [i[0] for i in list(itertools.groupby(stack))]
        while grouped[-1] == "+":
            grouped.pop()
        answer = len(grouped)
    print "Case #%s: %s" % (case + 1, answer)

