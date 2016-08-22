counter = 0

def main():
	global counter
	solutions = []
	with open('B-large.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			pans = f.readline().strip()
			counter = 0
			while len(pans) > 0:
				if pans[-1] == '+':
					pans = pans[:-1]
				else:
					pans = swap_first_pluses(pans)
					pans = do_swap(pans)
			solutions.append(str(counter))
			
	with open('B-large.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1
			
def swap_first_pluses(pans):
	global counter
	first_pluses = 0
	
	for c in pans:
		if c == '+':
			first_pluses += 1
			did_swap = True
		else:
			break
	
	if first_pluses > 0:
		counter += 1
		return '-'*first_pluses + pans[first_pluses:]
	else:
		return pans

def do_swap(pans):
	global counter
	swapped = ''
	for c in pans:
		if c == '+':
			swapped = '-' + swapped
		else:
			swapped = '+' + swapped
	counter += 1
	return swapped
	
main()
