

def flip(pancakes):
    pointer = 0
    count = 0

    if pancakes[pointer] == '-':
        while pointer < len(pancakes) and pancakes[pointer] == '-':
            pointer += 1
        count += 1
        if pointer == len(pancakes):
            return count

    #if pancakes[pointer] == '+': #always true
    while True:
        while pancakes[pointer] == '+':
            pointer += 1
            if pointer == len(pancakes):  # we hit the bottom and they are the right way up
                return count
        count += 1 # flip these to unhappy side
        while pointer < len(pancakes) and pancakes[pointer] == '-':
            pointer += 1
        count += 1 # flip this stack and the previous happy stack

        if pointer == len(pancakes):
            return count





#with open('sample_pan.in') as f:
#with open('B-small-attempt0.in') as f:
with open('B-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        pancakes = f.readline().strip()
        flips = flip(pancakes)

        print('Case #%s: %i' % (str(puzzle_count + 1), flips))
