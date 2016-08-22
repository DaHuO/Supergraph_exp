def flip(L, i):
    """Flips and reverses a list of booleans up to i."""
    return list(reversed([not x for x in L[:i]])) + L[i:]


def main():
    answers = []
    translate = {True: '+', False: '-'}
    for case in range(int(input())):
        pancakes = [p == '+' for p in input()]
        flips = 0
        while not all(pancakes):
            if pancakes[0]:
                pancakes = flip(pancakes, pancakes.index(False))
            elif True in pancakes:
                pancakes = flip(pancakes, pancakes.index(True))
            else:
                pancakes = flip(pancakes, len(pancakes))
            flips += 1
        answers.append(flips)
    for i, a in enumerate(answers):
        print('Case #{}: {}'.format(i + 1, a))

if __name__ == '__main__':
    main()
