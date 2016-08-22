#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compute_last_word(s):
    answer = s[0]
    for c in s[1:]:
        if answer[0] <= c:
            answer = c + answer
        else:
            answer += c
    return answer


def main():
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, compute_last_word(s)))


if __name__ == '__main__':
    main()
