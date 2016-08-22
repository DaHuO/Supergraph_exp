def convert(bn, base):
	ret = 0
	mul = 1
	while(bn):
		ret += mul * (bn & 1)
		mul *= base
		bn >>= 1
	return ret

def is_prime(n):
	i = 2
	while(i*i <= n):
		if(n%i == 0):
			return i
		i+=1

	return -1

def solve(N, J):
	max_x = (1 << N) - 1
	x = (1 << (N-1)) + 1
	count = 0
	ans = [0] * 11
	while(count < J and x <= max_x):
		s = ''
		flag = False
		for base in range(2,11):
			y = convert(x, base)
			a = is_prime(y)
			if a == -1:
				flag = True
				break
			ans[base] = a
		if not flag:
			s += str(convert(x,10)) + ' '
			for base in range(2,11):
				s+= str(ans[base]) + ' '
			print(s)
			count += 1
		x += 2

def main():
	t = int(input())
	N, J = tuple([int(i) for i in input().split()])
	print("Case #1:")
	solve(N,J)

if __name__ == '__main__':
	main()





