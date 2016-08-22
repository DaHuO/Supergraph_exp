
f = map(lambda x: x.strip(), open("test.in", "r").readlines()[1:])

def add(l, chars):
	if len(chars) == 0:
		return l
	new_l = []
	for i in l:
		new_l.append(i + chars[0])
		new_l.append(chars[0] + i)
	return add(new_l, chars[1:])

out = open("aOut.out", "w")

num = 1
for line in f:
	if len(line) == 1:
		word = line
	else:
		l = [line[0]]
		perms = add(l, line[1:])
		word = sorted(perms)[-1]
	out.write("Case #" + str(num) + ": " + word + "\n")
	num += 1