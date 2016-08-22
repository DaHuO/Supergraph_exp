from sets import Set 
filein = open('A-large.in', 'r')
fileout = open('A-large.out', 'w')
 
T = int(filein.readline())
for t in range(T):
    fileout.write('Case #%d: ' % (t + 1))
    s = filein.readline()
    result = ""
    for char in s:
    	if result == "":
    		result = result + char
    	elif char >= result[0]:
    		result = char + result
    	else:
    		result = result + char

    fileout.write(result)
 
filein.close()
fileout.close()