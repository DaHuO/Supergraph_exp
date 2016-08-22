

def solve_problem(problem_row):
    word = ""
    for c in problem_row:
        if len(word):
            first_char = word[0]
            if ord(c) >= ord(first_char):
                word = c + word
            else:
                word += c
        else:
            word += c
    return word


def parse_problems():
    t = int(raw_input())  # read a line with a single integer
    problems = []
    for _ in xrange(1, t + 1):
        _raw_input = raw_input()
        problems.append(_raw_input)
    return problems


problem_rows = parse_problems()
solutions = map(solve_problem, problem_rows)
for counter, solution in enumerate(solutions):
    print "Case #{}: {}".format(counter+1, solution)
