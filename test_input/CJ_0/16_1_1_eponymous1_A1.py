import sys
from collections import deque
def last_word( S ):
  word = deque(S[0])
  for ch in S[1:]:
    if ch >= word[0]:
      word.appendleft(ch)
    else:
      word.append(ch)

  return ''.join(word)

# get input filename from first arg
in_path = sys.argv[1]
# read input text file to list of strings, 1 per line; skip [0]: 'T'
with open(in_path, 'r') as in_file:
  in_list = in_file.read().splitlines()

# convert strings to ints (and skip first string)
in_list = [s for s in in_list[1:] ]

#print in_list

out_list = [ last_word(list(s)) for s in in_list ]

for i, x in enumerate(out_list):
  print 'Case #{}: {}'.format(i+1, x)
