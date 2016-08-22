import sys
from collections import deque

def get_last_word(S):
    new_word = deque()
    new_word.append(S[0])
    first_letter = S[0]

    for i in xrange(1,len(S)):
        if (first_letter > S[i]):
            new_word.append(S[i])
        else:
            new_word.appendleft(S[i])
            first_letter = S[i]

    return ''.join(new_word)




if __name__ == "__main__":

    T = int(sys.stdin.readline()) #number of test cases

    for i in xrange(1,T+1):
        S = sys.stdin.readline().strip()
        print 'Case #%d: %s' %(i,get_last_word(S))