import sys
from collections import deque
line_number = 0

for line in sys.stdin:
	if line_number:
		out = deque()
		out.append(line[0])
		for c in line[1:-1]:
			if c >= out[0]:
				out.appendleft(c)
			else:
				out.append(c)
		print("Case #%d: %s" % (line_number, "".join(list(out))))
	line_number += 1
