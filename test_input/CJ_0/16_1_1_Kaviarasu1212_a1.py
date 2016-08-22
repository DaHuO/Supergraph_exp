
def ip(word, rlist=None):
    if len(word) == 0:
        return rlist
    else:
        temp = []
        for i in rlist:
            temp.append(i + word[0])
            temp.append(word[0] + i)
        return (ip(word[1:], temp))

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  w = raw_input().strip()  # read a list of integers, 2 in this case
  ans = sorted(ip(w[1:], [w[0]]), reverse=True)[0]
  print "Case #{}: {}".format(i, ans)
