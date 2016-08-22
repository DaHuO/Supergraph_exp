#!/usr/bin/env python3


def create_word(S):
    words = [S[0]]
    for char in S[1:]:
        words_new = []
        for word in words:
            words_new.extend([word + char, char + word])
        words = words_new
    return sorted(words)[-1:][0]

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        print("Case #{0}: {1}".format(i, create_word(input())))
