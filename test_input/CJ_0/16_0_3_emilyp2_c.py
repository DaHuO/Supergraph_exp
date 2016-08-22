from math import sqrt

def is_jamcoin(bin_str):
	print(bin_str)
	if bin_str[0] != '1' or bin_str[len(bin_str)-1] != '1':
		return False
	facts = []
	for b in range(2, 11):
		gf = get_factor(int(bin_str, b))
		if gf:
			facts.append(gf)
		else:
			break
	if len(facts) == 9:
		str_facts = [str(a) for a in facts]
		fax = ' '.join(str_facts)
		return fax
	else:
		return False

def get_factor(num):
	num = float(num)
	for i in range(2, int(sqrt(num))):
		a = num/i
		if int(a) == a:
			return int(a)
	return False

fi = open('C-small-attempt0.in', 'r')
fo = open('cS.out', 'w')

T = fi.readline()
T = int(T)

for x in range(1,T+1):
	numbs = fi.readline()
	numbsl = numbs.split(' ')
	N = int(numbsl[0])
	J = int(numbsl[1])

	fo.write('Case #'+str(x)+':\n')

	found = 0
	s = '1' + '0'*(N-2) + '1'
	s = int(s, 2)

	while found < J:
		s += 2
		sb = str(bin(s))[2:]
		fax = is_jamcoin(sb)
		if fax:
			fo.write(sb + ' ' + fax + '\n')
			found += 1

fi.close()
fo.close()

