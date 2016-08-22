import itertools


def main():
	solutions = []
	with open('C-small-attempt1.in', 'r') as f:
		rows = int(f.readline())
		for i in range(rows):
			tc = f.readline().split(' ')
			N = int(tc[0])
			J = int(tc[1])
			all_elements = map(convert_element, ["".join(seq) for seq in itertools.product("01", repeat=N-2)])
			
			for current_element in all_elements:
				element_solution = check_element(current_element)
				if element_solution != None:
					solutions.append([current_element] + element_solution)
					if len(solutions) >= J:
						break
						
	with open('C-small-attempt1.out', 'w') as f:
		f.write("Case #1:\n")
		for line in solutions:
			line = map(str, line)
			f.write(" ".join(line) + '\n')
			
			
def convert_element(x):
	return '1'+x+'1'

def check_element(el):
	el_collection = []
	
	res_base2 = isprime(int(el, 2))
	if res_base2 == 0:
		return None
	el_collection.append(res_base2)
	
	res_base3 = isprime(int(el, 3))
	if res_base3 == 0:
		return None
	el_collection.append(res_base3)
	
	res_base4 = isprime(int(el, 4))
	if res_base4 == 0:
		return None
	el_collection.append(res_base4)
	
	res_base5 = isprime(int(el, 5))
	if res_base5 == 0:
		return None
	el_collection.append(res_base5)
	
	res_base6 = isprime(int(el, 6))
	if res_base6 == 0:
		return None
	el_collection.append(res_base6)
	
	res_base7 = isprime(int(el, 7))
	if res_base7 == 0:
		return None
	el_collection.append(res_base7)
	
	res_base8 = isprime(int(el, 8))
	if res_base8 == 0:
		return None
	el_collection.append(res_base8)
	
	res_base9 = isprime(int(el, 9))
	if res_base9 == 0:
		return None
	el_collection.append(res_base9)
	
	res_base10 = isprime(int(el))
	if res_base10 == 0:
		return None
	el_collection.append(res_base10)
	
	return el_collection
	    
def isprime(n):
    n = int(n)
    if n == 2:
        return 0
    if n == 3:
        return 0
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += w
        w = 6 - w
    return 0
    
main()
