
def trees(items, index, stri):
	if index > len(items) - 1:
		return stri
	else:
		s1 = trees(items, index+1, stri + items[index])
		s2 = trees(items, index+1, items[index] + stri)
		if s1 > s2:
			return s1
		else:
			return s2

f = open('A-small-attempt1.in', 'r')
o = open("o.txt", "w")
f = f.readlines()[1:]		

for i, t in enumerate(f):
	t = list(t)[:len(t) - 1]
	#print trees(t, 0, '')
	o.write("Case #" + str(i+1) + ": " + trees(t, 0, '') + "\n")