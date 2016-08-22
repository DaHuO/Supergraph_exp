def flip(pancakes, flip_point):
    for i in xrange(flip_point + 1):
        pancakes[i] = not pancakes[i]

def find_flip_point(pancakes):
    downside_found = False
    for (i, pancake) in enumerate(pancakes):
        if not pancake:
            downside_found = True # found the first face-down pancake
        else:
            if downside_found is True: # continuous face-down pancakes block ends here, flip here
                return i - 1
    return i # continuous at the bottom of the pancakes

def main():
    num_input = int(raw_input())

    for test_case_num in xrange(1, num_input + 1):
        pancakes = [ True if i == '+' else False for i in (raw_input().strip()) ]
        flip_count = 0
        while not all(pancakes):
            flip(pancakes, find_flip_point(pancakes))
            flip_count += 1
        print "Case #%d: %d" % (test_case_num, flip_count)

if __name__ == '__main__':
    main()