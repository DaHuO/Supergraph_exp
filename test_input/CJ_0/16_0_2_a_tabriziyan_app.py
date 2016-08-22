# coding=utf-8

import sys


def flip(pancake_list):
    pancake_list.reverse()

    return [-i for i in pancake_list]


def solve(pancake_list, flip_count):
    x = pancake_list[0]
    x *= -1

    try:
        index = pancake_list.index(x)
        pancake_list[:index] = flip(pancake_list[:index])
        flip_count += 1

        return solve(pancake_list, flip_count)
    except:
        if x == 1:
            return flip_count + 1
        else:
            return flip_count


def main():
    T = int(raw_input())
    for i in range(0, T, 1):
        pancake_list = []
        line = raw_input()
        for j in line:
            if j == '+':
                pancake_list.append(1)
            else:
                pancake_list.append(-1)

        print "Case #{}: {}".format(i + 1, solve(pancake_list, 0))


if __name__ == '__main__':
    sys.exit(main())
