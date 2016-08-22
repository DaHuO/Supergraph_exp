import math;

def primalty (number):
	for i in range (2, int (math.sqrt (number) + 1)):
		if (number % i == 0):
			return ( (False, i) );
	return ( (True, None) );

def validate (string):
	results = [];
	for i in range (2, 11):
		interpreted_number = int (string, i);
		is_prime, factor = primalty (interpreted_number);

		if (is_prime):
			return ( (False, None) );
		results.append (factor);
	return (True, results);

def get_jamcoins (length, min_count):
	combs = [bin(x)[2:].rjust(length, '0') for x in range(2**length)];
	results = [];

	for num in combs:
		if (not (num [0] == '1' and num [-1] == '1') ):
			continue;
		test = validate (num);
		if (test [0]):
			results.append ( (num, test [1]) );
		if (len (results) == min_count):
			break;

	return (results);

tc, length, min_count = 1, 16, 50;

print ('Case #1:');
for coin in get_jamcoins (length, min_count):
	print (coin [0], ' '.join ([str(i) for i in coin [1]]));