from collections import deque

def last_word(s): 
	d = deque()

	for c in s: 
		if len(d) == 0: 
			d.append(c)
		elif c >= d[0]: 
			d.appendleft(c)
		else:
			d.append(c)

	return ''.join(d)

if __name__ == '__main__': 
	f2 = open('output2.txt', 'w')

	with open('A-large.in', 'r') as f: 
		count = 0 

		for line in f: 
			if count == 0: 
				pass 
			else: 
				s = line.strip()
				f2.write('Case #{}: {}\n'.format(count, last_word(s)))

			count += 1