
def gen_string(s):

	sl = []

	s = list(s)

	for es in s:
		tsl = [ t for t in sl]
		nl = []
		for esl in tsl:
			org = esl
			s1 = esl+es
			s2 = es+esl

			# print esl,sl,s1,s2
			nl.append(s1)
			nl.append(s2)
			# sl.append(s1)
			# sl.append(s2)
			# sl.remove(org)
			# print sl
			# s = raw_input()
		sl = nl
		if sl == []:
			sl.append(es)

	return sl


def get_ans(s):
	ss = gen_string(s)

	ss.sort()
	return ss[-1]

f = open("A-small-attempt0.in" , "r")

lines = f.readlines()

N = int(lines[0])

for i in range(N):
	s = lines[i+1].split("\n")[0]
	# print s

	ans = get_ans(s)

	ans = "Case #"+str(i+1)+": "+str(ans)
	print ans
	# exit()