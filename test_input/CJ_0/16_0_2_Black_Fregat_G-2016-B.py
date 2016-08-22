import operator as op
with open("/storage/emulated/0/Download/B-large.txt", "r") as inf:
  with open("/storage/emulated/0/Download/B-out", "w") as outf:
    t, = map(int, inf.readline().split())
    for tt in range(t):
	    ln = inf.readline().strip()
	    cnt = sum(map(op.ne, ln[0]+ln, ln+"+"))
	    outf.write("Case #{0}: {1}\n".format(tt+1, cnt))

