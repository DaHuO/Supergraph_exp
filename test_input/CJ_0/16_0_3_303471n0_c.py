from pr import primecheck as pc
o = open("o.txt", "w")
o.write("Case #1:\n")
x = "0b1000000000000001"
x = int(x, 2)
xy = "0b10000000000000001"
xy = int(xy, 2)
j = 0

while int(x) < int(xy) and j < 50:
	c = str(bin(x)[2:])
	for z in range(2, 11):
		pcheck = int(bin(x)[2:], z)
		if pcheck%2 == 1 and pc(pcheck):
			c = ''
			break
		else:
			d = 2
			while pcheck%d != 0:
				d += 1
			c = c + " " + str(d)
	if c:
		j += 1
		o.write( c + "\n")
	x += 2