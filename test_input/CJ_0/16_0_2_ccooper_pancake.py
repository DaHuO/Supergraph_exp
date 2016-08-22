import sys

lines = sys.stdin.readlines()

line_num = 0

test_cases = int(lines[line_num])
line_num += 1

for test_case in range(0, test_cases):
    start = lines[line_num].strip()
    line_num += 1

    seen = {}
    seen[start] = 0
    work_items = [(start, 0)]

    while(work_items):
        (original, best_case) = work_items.pop(0)

        ##print "original = '%s'" % (original)
        for i in range(0, len(original)):
            flipped = ""
            for j in range(0, i + 1):
                flipped += ('+', '-')[original[i - j] == '+']
            flipped += original[i + 1:]
            ##print "flipped(%d) = '%s'" % (i, flipped)
            if flipped in seen:
                seen_best_case = seen[flipped]
                if seen_best_case <= best_case + 1:
                    continue
            seen[flipped] = best_case + 1
            work_items += [(flipped, best_case + 1)]                    

    goal = "+" * len(start)
    best_case = seen[goal]
    print "Case #%d: %d" % (test_case + 1, best_case)