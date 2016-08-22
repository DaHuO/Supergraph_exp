from sys import argv
import math
def is_prime(x):
	for i in range(2, int(math.sqrt(x))+1):
		if x % i ==0:
			return i
	return 0

def binary(x):
	ans = ""
	while x > 0:
		ans = str(x%2)+ans
		x /= 2
	return ans

def base(x, ba):
	bb = 1
	ans = 0
	for c in x:
		ans += int(c)*bb
		bb *= ba
	return ans

if __name__ == "__main__":
	inf = open(argv[1], 'r')
	lines = inf.readlines()
	inf.close()
	T = int(lines[0][:-1])
	para = lines[1][:-1].split(' ')
	N, J = int(para[0]), int(para[1])
	ouf = open(argv[2], 'w')
	ouf.write("Case #1:\n")
	low = pow(2, N-1)+1
	high = pow(2, N)-1
	for x in range(low, high+1, 2):
		print x
		fac = is_prime(x)
		dic = {}
		if fac > 0:
			dic[2] = fac
			b_st = binary(x)
			for i in range(3, 11):
				v = base(b_st[::-1], i)
				fac = is_prime(v)
				if fac > 0:
					dic[i] = fac
				else:
					break
			if fac > 0:
				ouf.write(b_st)
				for i in range(2, 11):
					ouf.write(" "+str(dic[i]))
				ouf.write("\n")
				J -= 1
				if J == 0:
					break

	ouf.close()