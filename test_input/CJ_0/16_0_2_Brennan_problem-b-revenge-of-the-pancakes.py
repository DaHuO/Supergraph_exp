
from string import maketrans

num_problems = int(raw_input())
problems = [raw_input() for i in xrange(num_problems)]


def calculate_required_flips(puzzle):
    mapping = maketrans('-+', '+-')
    x = 0
    while True:
        index_of_last_sad_pancake = puzzle.rfind("-")
        if index_of_last_sad_pancake == -1:
            break
        puzzle = "%s%s" % (str(puzzle[:index_of_last_sad_pancake+1]).translate(mapping),
                           puzzle[index_of_last_sad_pancake+1:])
        x += 1
    return x


for i, problem in enumerate(problems):
    min_required_flips = calculate_required_flips(problem)
    print "Case #%s: %s" % (i+1, min_required_flips)

