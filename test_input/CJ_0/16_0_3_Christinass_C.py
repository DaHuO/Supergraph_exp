import random

N = 32

ans = []
dic = set()
while len(ans) < 500:
	s = '1' + ''.join([random.choice('01') for i in range(N - 2)]) + '1'
	# print s
	ret = [s]

	for x in xrange(2, 11):
		t = int(s, x)
		for i in xrange(2, min(t, 5000)):
			if t % i == 0:
				ret.append(i)
				break
		else:
			break
	if len(ret) == 10 and ret[0] not in dic:
		dic.add(ret[0])
		ans.append(ret)

out = open("out.txt", "w")
# print("Case #1:")
out.write("Case #1:\n")
for item in ans:
	# print(' '.join(map(str, item)))
	out.write(' '.join(map(str, item)) + '\n')