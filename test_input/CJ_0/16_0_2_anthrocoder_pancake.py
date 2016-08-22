import sys

try: 
	f = open(sys.argv[1])
	out = open(sys.argv[1].rpartition("\\")[2]+".out", 'w')

	numTests = int(f.readline())

	for i in range (0, numTests):
		plate = f.readline()
		#print (plate)
		plate = plate[::-1]
		#print (plate)
		numflips = 0

		for j in range (0, len(plate)):
			if plate[j] == '-':
				plate = plate.replace('-', 'a')
				plate = plate.replace('+', '-')
				plate = plate.replace('a', '+')
				numflips += 1
		
		
		out.write("Case #" + str(i+1) +": " + str(numflips) + "\n")


except IOError as e:
	print ('Error:', err) 

