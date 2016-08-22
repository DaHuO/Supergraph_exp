import math
N = 16
J = 50

def main():
	outfile = open('results', 'w')
	outfile.write('Case #1:\n')
	
	middle_num = 0
	found = 0
	while found < J:
		coin = '1' + ('{0:0%ib}' %(N - 2)).format(middle_num) + '1'
		test = test_bases(coin)
		if test != '':
			outfile.write(coin + test + '\n')
			found += 1
		middle_num += 1

def test_bases(coin):
	factor_list = ''
	for i in range(2, 11):
		factor = get_factor(to_base_ten(coin, i))
		if factor == 0:
			return ''
		else:
			factor_list += ' %i' %(factor)
	return factor_list

def to_base_ten(strnum, original_base):
	result = 0
	length = len(strnum) - 1
	for i in range(length + 1):
		result += int(strnum[i]) * original_base ** (length - i)
	return result
	
def get_factor(num):
	if (num % 2) == 0:
		return 2
	if (num % 3) == 0:
		return 3
	for i in range(1, int(math.sqrt(num) + 2)):
		if (num % (6*i-1)) == 0:
			return 6*i - 1
		if (num % (6*i+1)) == 0:
			return 6 * i + 1
	return 0

main()
