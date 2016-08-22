# -*- coding: utf-8 -*-

from pprint import pprint as _p


def get_pancakes(line):
    v = []
    for p in line:
        if p == '-':
            v.append(0)
        elif p == '+':
            v.append(1)
    return v


def flipp(values, n):
    l = 0
    r = n
    while l <= r:
        if l != r:
            buff = values[r]
            values[r] = int(not values[l])
            values[l] = int(not buff)
        else:
            values[r] = int(not values[l])
        l += 1
        r -= 1
    return values


def happy(values):
    return all(values)


def print_pancakes(values):
    print ''.join('+' if x else '-' for x in values)


def main():
    with open('2016_b.in') as f:
        with open('2016_b.out', 'w') as fo:
            lines = f.readlines()
            for t in range(1, int(lines[0].strip()) + 1):
                pancakes = get_pancakes(lines[t].strip())
                if len(pancakes) == 1:
                    if happy(pancakes):
                        fo.write('Case #{}: {}\n'.format(t, 0))
                    else:
                        fo.write('Case #{}: {}\n'.format(t, 1))
                else:
                    flipps = 0
                    j = len(pancakes) - 1
                    while not happy(pancakes):
                        # print_pancakes(pancakes)
                        while pancakes[j]:
                            j -= 1
                        i = j
                        while pancakes[i] != pancakes[0]:
                            i -= 1
                        pancakes = flipp(pancakes, i)
                        flipps += 1
                    fo.write('Case #{}: {}\n'.format(t, flipps))


if __name__ == '__main__':
    main()













