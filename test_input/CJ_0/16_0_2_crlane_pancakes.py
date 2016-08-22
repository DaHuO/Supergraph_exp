import sys

TEST_FILENAME = 'test_cakes.in'


def solve(pancakes):
    UP = 1
    DOWN = -1
    i = 0
    while sum(pancakes) != len(pancakes):
        j = 0

        if pancakes[0] == UP:
            # find the first negative
            while j < len(pancakes) and pancakes[j] == UP:
                pancakes[j] *= -1
                j += 1
            # also flip first negative
            # pancakes[j] *= -1
        else:
            while j < len(pancakes) and pancakes[j] == DOWN:
                pancakes[j] *= -1
                j += 1
        i += 1

    return i


def read_input_and_solve(filename):
    UPSTRING = '+'
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if not i:
                T = int(line.strip())
            else:
                cakestring = line.strip()
                cakes = [1 if p == UPSTRING else -1 for p in cakestring]
                assert len(cakestring) == len(cakes)
                print 'Case #{}: {}'.format(i, solve(cakes))


if __name__ == '__main__':
     if len(sys.argv) > 1:
         f = sys.argv[1]
     else:
         f = TEST_FILENAME
     read_input_and_solve(f)
