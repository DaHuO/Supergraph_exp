#!/usr/bin/python
import sys
import binascii

#
def readFile(file):
	# lines(file)
	lines = [];
	for line in file:
		# print line
		lines.append(line)
	return lines;


def lastStr(s):
	rst = ""
	for i in range(0, len(s)):
		c = s[i]
		if(len(rst) > 0 and c >= rst[0]):
			rst = c + rst
		else:
			rst = rst + c
	return rst






def main():
    file = open(sys.argv[1], "r+")
    rfile = open(sys.argv[2],'r+')
    print "file name: ", file.name
    lines = readFile(file)
    testNum = int(lines[0])
    print "testTotal:", testNum
    for i in range(1, testNum+1):
    	s = lines[i].strip()
    	r = lastStr(s)
    	r = "Case #"+str(i)+": " + str(r)
    	rfile.write(r+"\n")
    	



if __name__ == '__main__':
    main()