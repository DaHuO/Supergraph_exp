
def main():
	solutions = []
	with open('A-large.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			result = ''
			tc = f.readline().strip()
			
			for letter in tc:
				if result == '' or result[0] > letter:
					result = result + letter
				else:
					result = letter + result
			
			solutions.append(result)
	
	with open('A-large.out', 'w') as f:
		counter = 1
		for line in solutions:
			f.write("Case #{0}: {1}\n".format(str(counter), line))
			counter += 1



main()
