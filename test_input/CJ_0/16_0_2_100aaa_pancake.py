import sys

def main(argv=sys.argv):
    output = open("B-large.out", "w")
    input = open("B-large.in", "r")
    number_of_tescases = int(input.readline())
    case = 1
    for case in range(1, number_of_tescases + 1):
        pancakes = input.readline()
        pancakes = pancakes.rstrip()
        trials = solve(pancakes.rstrip())
        output.write("Case #" + str(case) + ": " + str(trials) + "\n")
    output.close()
    input.close()

def solve(pancakes):
    pancakes = simplify_stack(pancakes)
    if len(pancakes) == 1 and pancakes == '+':
        return 0
    elif len(pancakes) == 1 and pancakes == '-':
        return 1
    else:
        flip = 0
        while True:
            if determin_all_happy_side(pancakes) == True:
                return flip
            scoop_pointer = get_flipping_position(pancakes)
            pancakes = flip_pancake(pancakes, scoop_pointer)
            flip = flip + 1

def get_flipping_position(pancakes):
    all_minus = True
    for idx, char in enumerate(pancakes):
        if char == '+':
            all_minus = False
            break
    if all_minus == True:
        return len(pancakes) - 1

    start = pancakes[0]
    for idx, char in enumerate(pancakes):
        if idx + 1 == len(pancakes):
            return None
        if pancakes[idx] != pancakes[idx+1]:
            return idx


def simplify_stack(pancakes):
    for idx, char in enumerate(pancakes):
        try:
            if char == pancakes[idx + 1]:
                del pancakes[idx+1]
        except Exception as e:
            # out of index
            pass
    return pancakes


def determin_all_happy_side(pancake):
    for idx, char in enumerate(pancake):
        if char == '-':
            return False
    return True

def flip_pancake(pancakes, scoop_pointer):
    pancakes = list(pancakes)
    for idx, char in enumerate(pancakes):
        if char == '+':
            pancakes[idx] = '-'
        else:
            pancakes[idx] = '+'
        if idx == scoop_pointer:
            break
    return "".join(pancakes)

if __name__ == "__main__":
    main()