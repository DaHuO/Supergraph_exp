import re

def flip(pancakes):

	if not '-' in pancakes:
		return 0
	if not '+' in pancakes:
		return 1

	current = pancakes[0]
	flips = 0
	for i in range(1, len(pancakes)):
		new = pancakes[i]
		if new != current:
			flips += 1
		current = new

	if pancakes[-1] == '-':
		flips += 1

	return flips

if __name__ == "__main__":
	with open('B-large.in', 'r') as doc:
		with open('bout.txt', 'w') as bout:

			cases = int(doc.readline())

			for i in range(1, cases+1):
				pancakes = doc.readline().rstrip()
				bout.write("Case #{}: {}\n".format(i, flip(pancakes)))