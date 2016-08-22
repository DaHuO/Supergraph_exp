testcase_count = int(input())
for testcase_index in range(testcase_count):
	stack = input()
	maneuvers = 0
	while "-" in stack:
		maneuvers += 1
		if stack[0] == "+":
			#flip the smiley pancakes on top
			flip_size = 0
			while stack[flip_size] == "+":
				flip_size += 1
			stack = "-" * flip_size + stack[flip_size:]
		else:
			#flip all except the bottom smileys
			flip_size = len(stack)
			while stack[flip_size - 1] == "+":
				flip_size -= 1
			flipped = ""
			for index in range(flip_size):
				flipped = ("+" if stack[index] == "-" else "-") + flipped
			stack = flipped + stack[flip_size:]
	print("Case #%d: %d" % (testcase_index + 1, maneuvers))