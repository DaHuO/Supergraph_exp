#!/usr/bin/python3


def get_output(input_val):
    if input_val == "":
        return ""
    last_word = input_val[0]
    for s in input_val[1:]:
        if s >= last_word[0]:
            last_word = s + last_word
        else:
            last_word += s
    return last_word

if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, get_output(input())))
