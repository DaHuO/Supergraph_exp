#! /usr/bin/python
import sys

if __name__ == "__main__":
    num_tests = int(sys.stdin.readline())
    for test_number in range(1, num_tests + 1):
        s = sys.stdin.readline().strip()
        last_word = s[0]
        for x in s[1:]:
            if x >= last_word[0]:
                last_word = x + last_word
            else:
                last_word = last_word + x
                
        print("Case #{}: {}".format(test_number, last_word))
        