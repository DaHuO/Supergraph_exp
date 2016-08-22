def bin(c):
   bincon = "01"
   if c < 2:
      return str(c)
   else:
      return bin(c//2) + str(c%2)
def decv(n, base):
	dv = 0
	sn = str(n)
	for x in range(len(sn)):
		umv = int(sn[-(x+1)])
		dv+=umv*base**x
	return dv
def prc(n):
	for x in range(2,1000):
		if n%x ==0:
			prod = x
			break
		else:
			prod = False
	return prod
def posjamcogen(leng, seed):
	withones = '1'+(leng-2-len(seed))*'0'+seed+'1'
	return int(withones)
outfile = open('/root/Desktop/outfile.txt', 'w')
outfile.write('Case #1:\n')
j = 0
l = 32
c = 0
while j<500:
	binnum = bin(c)
	posjamco = posjamcogen(l, binnum)
	fl = [posjamco]
	for base in range(2,11):
		cpr = prc(decv(posjamco, base))
		print j
		if not cpr:
			break
		fl.append(str(cpr))
		if base == 10:
			for obj in fl:
				outfile.write(str(obj)+' ')
			outfile.write('\n')
			j+=1
	c+=1
outfile.close()
