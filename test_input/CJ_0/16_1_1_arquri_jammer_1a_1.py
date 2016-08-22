import sys, os
import requests
import urllib
import types
import re
import math
from operator import itemgetter

handle = open("A-large (1).in","r")
allconts = handle.read().split("\n")
handle.close()

T = int(allconts[0])
results = []

for i in range(0,T):
	sequence = str(allconts[i+1])
	seqlen = len(sequence)
	netstr = sequence[0]
	for k in range(1,seqlen):
		curchar = sequence[k]
		if ord(netstr[0])>ord(curchar):
			netstr = netstr + curchar
		else:
			netstr = curchar + netstr
	results.append(netstr)
	
handle = open("jammer_1a_1.txt","w")
for i in range(0,len(results)):
	handle.write("Case #"+str(i+1)+": "+results[i]+"\n")
handle.close()
	
	