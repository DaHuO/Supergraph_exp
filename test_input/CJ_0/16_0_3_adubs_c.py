import sys
import math

n = 16
j = 50

print("Case #1:")
for i in range(1, int(math.pow(2, n))):
	iStr = '{:016b}'.format(i)
	if iStr[0] != '1' or iStr[n-1] != '1':
		continue
	output = iStr
	for base in range(2, 11):
		valueInBase = 0
		exp = 0
		for char in reversed(list(iStr)):
			valueInBase += int(math.pow(base,exp)) * int(char)
			exp += 1
		divisorFound = False
		for divisor in range(2, int(math.sqrt(valueInBase))):
			if valueInBase % divisor == 0:
				output += " " + str(divisor)
				divisorFound = True
				break
		if not divisorFound:
			break
		if divisorFound and base == 10:
			print(output)
			j -= 1
	if j == 0:
		break