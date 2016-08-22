
def solve(s):
	s = s[::-1]
	flips = 0
	for c in s:
		flips += calc_flip(c,flips)
	return flips

def calc_flip(c,flips): 
	if flips%2 == 0:
		if c == "-":
			return 1
	else:
		if c == "+":
			return 1
	return 0

def main():
    t = int(input())
    for i in range(0,t):
        s = input()
        result = solve(s)
        print("Case #%d: %d"%(i+1,result))

if __name__ == "__main__" :
    main()
