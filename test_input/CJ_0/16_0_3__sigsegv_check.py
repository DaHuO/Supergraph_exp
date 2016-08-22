import sys

coins = []

def checkBase(jcoin, divisor, base):
	if not int(jcoin, base) % divisor == 0:
		print("\t%s (%s) %s %s" % (jcoin, int(jcoin, base), base, divisor))
		return False
	return True
	

def check(jcoin, divisors):
	valid = True
	if jcoin in coins:
		valid = False
		print("<<duplicate coin>>")
	if str(jcoin)[0] != '1' or str(jcoin)[-1] != '1':
		valid = False
		print("<<jcoins must start and end with 1>>")
	coins.append(jcoin)
	for i in range(9):
		valid &= checkBase(jcoin, divisors[i], i + 2)
	return valid

def checkCase(case):
	splitCase = case.rstrip().split(" ")
	jcoin = splitCase[0]
	divisors = list(map(int, splitCase[1:]))
	valid = check(jcoin, divisors)
	if (valid):
		print("- - Valid - - " + str(jcoin))
	else:
		print("***INVALID*** " + str(jcoin))
	return valid


fname = sys.argv[1]
f = open(fname, "r")
next(f)
all_valid = True
for line in f:
	all_valid &= checkCase(line)
print("OVERALL: %s" % ("valid" if all_valid else "INVALID"))
f.close()
