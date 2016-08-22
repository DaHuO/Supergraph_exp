class Flipper():
	def __init__(self, stack):
		self.flips = 0
		self.n = "-"
		self.p = "+"
		self.stack = stack

	def count_flips(self):
		l = len(self.stack) - 1
		while l >= 0:
			if self.stack[l] == self.n:
				self.flip()
			l -= 1
		return self.flips


	def flip(self):
		self.flips += 1
		self.n, self.p = self.p, self.n

def main():
	t = int(input())
	for i in range(1, t+1):
		x = input()
		flips = Flipper(x).count_flips()
		print("case #{}: {}".format(i, flips))

if __name__ == "__main__":
	main()