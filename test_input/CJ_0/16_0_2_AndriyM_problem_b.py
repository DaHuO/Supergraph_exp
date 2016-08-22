

def min_flips(stack):
    if len(stack) == 0:
        return 0
    last_pancake = stack[0]
    flips = 1 if last_pancake == '-' else 0
    for s in stack[1:]:
        if s == last_pancake:
            continue
        elif s == '-' and last_pancake == '+':
            flips += 2

        last_pancake = s
    return flips

if __name__ == '__main__':
    # print(min_flips('-'))
    # print(min_flips('+'))
    # print(min_flips('--'))
    # print(min_flips('++'))
    # print(min_flips('--+-'))

    with open('B-large.in', 'r') as inp:
        lines = inp.readlines()

    T = int(lines[0])
    with open('B-large.out', 'w') as out:
        for i in range(1, T + 1):
            out.write('Case #%d: %s\n' % (i, min_flips(lines[i].strip())))
