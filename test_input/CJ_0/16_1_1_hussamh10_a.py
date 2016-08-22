def main():

	f = open('input.txt', 'r')
	o = open('output.txt', 'w')

	tc = int(f.readline())
	k = 0

	while (tc > 0):

		k += 1
		s = str(f.readline())
		print (s)
		length = len(s)
		i = 0
		out = '0'

		while(length > 0):
			c = s[i]
			i+= 1

			if(out == '0'):
				out = c

			elif (ord(c) >= ord(out[0])):
				out = c + out


			elif (ord(c) <= ord(out[0])):
				out = out + c

			length -= 1



		wr = 'Case #' + str(k) + ': ' + out  

		o.write(wr)
		tc -= 1
	



main()
