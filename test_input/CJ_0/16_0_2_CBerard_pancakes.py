import numpy as np
import sys

def checkeq(list):
    if (list[1:] == list[:-1]):
    	return 1
    else:
    	return 0

def getlowest(list):
	# return position of lowest "-"
	#print "LIST TO GET LOWEST=",list
	#print "LIST WHEN FLIPPED=",list[::-1]
	n = len(list)
	flippedlist=list[::-1] #flip list -- now get first "-"
	for i in range(n):
		#print flippedlist[i],n-i
		if flippedlist[i]=="-":
			#print "new lowest=",n-i
			return n-i

def flip(list):
	lowest = getlowest(list)-1
	#print "list before ",list
	for i in range(lowest+1):
		if (list[i]=="-"):
			list[i] = "+"
		elif (list[i] == "+"):
			list[i] = "-"
	#print "list after ",list
	return list

#need to output number of maneuvers
def doflips(order):
	# order -- input order of happy/sad pancakes
	orderlist=list(order)
	if (checkeq(orderlist)==1):
		if orderlist[0] =="-":
			return 1
		else:
			return 0 # 0 maneuvers needed

	#now execute flips
	movecount=0
	while checkeq(orderlist)==0:
		flip(orderlist)
		movecount += 1
		if checkeq(orderlist)==1:
			return movecount
	return

inputs=np.loadtxt("./pancakein.txt",skiprows=1,dtype=str,unpack=True)
numtests=int(inputs[0])
sides=inputs[1:]

fout = open("./pancakeout.txt","w")

for k in range(numtests):
	fout.write("Case #"+str(k+1)+": "+str(doflips(sides[k]))+"\n")

fout.close()