import sys

lines = []
for line in sys.stdin:
	lines.append(line.strip())

def next():
	return lines.pop(0)

def main():
	tc = int(next())
	for i in range(tc):
		print("Case #%d: "%(i+1)+str(foo(next())))


def foo(s):
	s = str(s)
	s2 = []
	for c in s:
		if len(s2) == 0 or c >= s2[0]:
			s2 = [c] + s2
		else:
			s2 = s2 + [c]
	return ''.join(s2)

if __name__ == "__main__":
	main()