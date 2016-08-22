#!/usr/bin/env python3


import sys


def get_cases():
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        yield sys.stdin.readline().strip()


def mutate(word, remaining_letters):
    if not remaining_letters:
        yield word
    else:
        pre = remaining_letters[0] + word
        post = word + remaining_letters[0]
        chosen = max(pre, post)

        if chosen > word:
            yield from mutate(chosen, remaining_letters[1:])


def solve_case(case):
    last_words = list(mutate(case[0], case[1:]))
    assert len(last_words) == 1
    return last_words[-1]


def main():
    sys.setrecursionlimit(2000)
    for index, case in enumerate(get_cases(), start=1):
        print("Case #{}: {}".format(index, solve_case(case)))


if __name__ == '__main__':
    main()
