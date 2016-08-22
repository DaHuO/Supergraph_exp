def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        cakes = content[i]
        last_flip = 1 if cakes[-1] == '-' else 0
        transition_count = 0
        for s_id in xrange(len(cakes) - 1):
            if cakes[s_id] != cakes[s_id + 1]:
                transition_count += 1
        print("Case #%s: %s" % (i, transition_count + last_flip))
        i += 1

filename = raw_input()
print_solutions(filename)
