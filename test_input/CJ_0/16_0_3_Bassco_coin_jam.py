#!/usr/bin/python
import thread
def base2dec(base, value, val_len):
	rev_val = list(value)
	rev_val.reverse()
	total = 0
	for i in xrange(val_len):
		total += (base**i)*int(rev_val[i])
	return total

def is_prime(number):
	limit = int(number**(0.5)) + 1
	for i in xrange(2, limit):
		if (number%i == 0):
			return False
	return True

def divisor(number):
	limit = (number/2)+1
	for i in xrange(2, number):
		if (number%i == 0):
			return i

def incr(val):
	rev_val = list(val)
	rev_val.reverse()
	func = lambda x,y: x+y
	for i in xrange(len(rev_val)):
		if rev_val[i]=='0':
			rev_val[i] = '1'
			for j in xrange(len(rev_val[:i])):
				rev_val[j] = '0'
			rev_val.reverse()
			return reduce(func, rev_val)
	rev_val.reverse()
	return reduce(func, rev_val)

if __name__=='__main__':
	
	t = int(raw_input())
	for i in xrange(t):
		input_r  = raw_input().split(' ')
		n = int(input_r[0])
		j = int(input_r[1])
		u_limit = n - 2
		i_value = '0'*u_limit
		curr_iter = 0
		print 'Case #'+str(i+1)+':'
		count = 0
		while count < j:
			value = '1'+i_value+'1'
			func = lambda x: base2dec(x, value, n)
			dec_list = map(func, range(2,11))
			prime_list = map(is_prime, dec_list)
			if not(True in prime_list):
				div_list = map(divisor, dec_list)
				print value +' '+ reduce(lambda x,y: str(x)+' '+str(y), div_list)
				count += 1
			
			if i_value == '1'*u_limit:
				break
			i_value = incr(i_value)
