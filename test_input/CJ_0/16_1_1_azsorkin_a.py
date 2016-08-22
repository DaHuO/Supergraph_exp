#! /usr/bin/env python

def main():
    num_cases = int(raw_input())
    for case in range(1, num_cases + 1):
        S = raw_input()
        frist = answer = S[0]
        for letter in S[1:]:
            if frist <= letter:
                frist = letter
                answer = letter + answer
            else:
                answer = answer + letter
        print 'Case #{}: {}'.format(case, answer)

if __name__ == '__main__':
    main()
