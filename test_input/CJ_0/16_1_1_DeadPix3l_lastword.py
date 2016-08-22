#!/usr/bin/env python2
with open('lastword.in','r') as f:
	_=f.readline()
	case=0
	for s in f:
		case+=1
		for i,v in enumerate(s):
			if i==0: 
				word=v
				continue
			if v>=word[0]: word= v+word
			else: word+=v 

		print "Case #{}: {}".format(case,word),
