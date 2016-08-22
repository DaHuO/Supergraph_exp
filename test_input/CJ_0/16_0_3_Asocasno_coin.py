import array;
import math;

def isprime(x):
	if((x % 2) == 0):
		return 2;
	for y in range(3, int(x**0.5)+1, 2):
		if not (x % y):
			return y;
	return 0;

def main():
	x = int(raw_input());
	text = raw_input();
	(length, need) = text.split();
	length = int(length);
	need = int(need);


	digits = length - 2;
	upto = (1 << digits);


	msb = [0,0];
	for x in range(2,11):
		msb.append(int(math.pow(x, length-1)) + 1);

	print "Case #1: ";

	for x in range(0, upto):
		x = format(x, 'b');
		values = [];
		valid = 1;
		for y in range(2,11):
			toAdd = (int(x,y)*y) + msb[y];
			factor = isprime(toAdd);
			#print "Base: " + str(y) + " value is: " + str(toAdd) + " and factor: " + str(factor);
			if(factor == 0):
				valid = 0;
				break;
			values.append(factor);
		if(valid == 1):
			num = str(x);
			while(len(num) < digits):
				num = "0" + num;
			print "1" + num + "1",
			for y in range(0,8):
				print str(values[y]),
			print values[8];
			need = need - 1;
		if(need == 0):
			break;

main();
