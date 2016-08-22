t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  S = raw_input()  # input num
  last_word = S[0]
  for j in range(1,len(S)):
      if S[j] < last_word[0]: last_word += S[j]
      else: last_word = S[j] + last_word
  print "Case #{}: {}".format(i, last_word)
