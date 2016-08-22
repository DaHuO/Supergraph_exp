import sys, os
import requests
import urllib
import types
import re
import math
from operator import itemgetter

handle = open("B-large.in","r")
allconts = handle.read().split("\n")
handle.close()

T = int(allconts[0])
results = []

for i in range(0,T):
	sequence = str(allconts[i+1])
	seqlen = len(sequence)
	moves = 0
	
	for k in range(0,1000):
		# check if the sequence is completed
		moves = k
		if sequence=="+"*seqlen:
			results.append(moves)
			break
		
		# check for symmetry
		if (seqlen%2)==0:
			positives = "+"*(len(sequence)/2)
			negatives = "-"*(len(sequence)/2)
			# check for negative-rigth symmetry
			if sequence[0:len(sequence)/2]==positives and sequence[(len(sequence)/2):]==negatives:
				moves += 2
				results.append(moves)
				break
			# check for positive-right symmetry	
			if sequence[0:len(sequence)/2]==negatives and sequence[(len(sequence)/2):]==positives:
				moves += 1
				results.append(moves)
				break
			
		# find the right-most negative and perform a flip
		rightNegPos = -1
		closestPost = 0
		for m in range(0,seqlen):
			if sequence[seqlen-m-1]=="-":
				closestPos = seqlen-m-1
				# don't allow recursives by symmetry.
				if sequence[0]=="+":
					continue
				rightNegPos = seqlen-m-1
				break
		if rightNegPos==-1:
			rightNegPos = closestPos-1
			
		# we have found the flipper point. Perform the flip
		flipPart = sequence[0:(rightNegPos+1)]
		remPart = sequence[(rightNegPos+1):]
		newStr = ""
		for m in range(0,len(flipPart)):
			if flipPart[m]=="+":
				newStr += "-"
			else:
				newStr += "+"
		flipPart = newStr[::-1]
		
		
		# check for symmetry in the flipper
		fliplen = len(flipPart)
		if (fliplen%2)==0:
			positives = "+"*(fliplen/2)
			negatives = "-"*(fliplen/2)
			# check for negative-rigth symmetry
			if flipPart[0:fliplen/2]==positives and flipPart[fliplen/2:]==negatives:
				moves += 2
				results.append(moves)
				break
			# check for positive-right symmetry	
			if flipPart[0:fliplen/2]==negatives and flipPart[fliplen/2:]==positives:
				moves += 1
				results.append(moves)
				break
		
		sequence = flipPart+remPart
		#if i==5:
		#	print flipPart+":"+remPart+":"+sequence
	

handle = open("jam_results_2_2.txt","w")
for i in range(0,T):
	handle.write("Case #"+str(i+1)+": "+str(results[i])+"\n")
handle.close()
