import math

def last_word(S):
    last_word = S[0]
    for i in S[1:]:
        if i >= last_word[0]:
            last_word = i + last_word
        else:
            last_word = last_word + i
    return last_word

def last_word_in():
    test_case_num = int(raw_input())
    for test_case in range(1, test_case_num+1):
            print 'Case #%s: %s' % (test_case, last_word(raw_input()))



last_word_in()