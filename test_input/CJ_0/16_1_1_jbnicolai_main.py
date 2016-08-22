import itertools
import sys

T = int(next(sys.stdin))

for t, S in enumerate(itertools.islice((S.strip() for S in sys.stdin), T), 1):

    last_word = S[0]

    for c in S[1:]:
        if c >= last_word[0]:
            last_word = c + last_word
        else:
            last_word = last_word + c

    print('Case #{:d}: {:s}'.format(t, last_word))
