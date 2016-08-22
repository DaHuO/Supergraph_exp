from sys import stdin

T = int(stdin.readline())

for t in range(T):
	pancakes = stdin.readline().strip()
	blocks = []

	current = pancakes[0]
	count = 1
	for p in pancakes[1:]:
		if p == current:
			count += 1
		else:
			blocks.append((current, count))

			current = p
			count = 1

	blocks.append((current, count))

	print("Case #{}: {}".format(t + 1, len(blocks) - (blocks[-1][0] == "+")))
