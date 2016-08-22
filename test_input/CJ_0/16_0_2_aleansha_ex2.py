import numpy as np

def get_data():
	filename = "B-large.in"
	data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
	process_data(data)

def process_data(data):
	index = 1
	for number in data:
		result = process_number(number)
		print('Case #%d: %s' %(index, result))
		index += 1
		

def process_number(number):
	it = 0
	nr = convert_number(number)
	summ = len(nr)
	while not np.sum(nr) == summ:
		if summ == 1:
			return 1
		for i in range(len(nr)-1, -1, -1):
			if not nr[i] == 1:
				#print(i, nr, np.multiply(nr[0:i+1], -1), nr[i:])
				nr = np.concatenate((np.multiply(nr[0:i+1], -1), nr[i+1:]), axis=0)
				it += 1
		break
	return it



def convert_number(number):
	nr = []
	for dig in number:
		if dig == '+':
			nr.append(1)
		else:
			nr.append(-1)
	return nr

if __name__ == '__main__':
	get_data()