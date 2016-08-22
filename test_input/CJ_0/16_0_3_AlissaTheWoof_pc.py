import math
out =open('./pcout.txt', 'w+')
t = input()
t = input()
out.write("Case #1: \n")

#this question... was not meant for people who write math contests.

for x in range(1, 501):
	number = "11"
	for y in range(1, 15):
		if ((x%pow(2, (15-y)))/math.pow(2,(14-y))) >= 1:
			number += "11"
		else:
			number += "00"
	number += "11"
	out.write(number)
	out.write(" 3 4 5 6 7 8 9 10 11") 
	out.write("\n")