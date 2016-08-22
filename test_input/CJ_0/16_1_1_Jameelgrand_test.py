#!/usr/bin/python
from collections import Counter
import sys
import string
input_list=[]
digs = string.digits + string.letters
def get_input(file_path):
	inputfile=open(file_path)
	for x in inputfile.readlines():
		try:
			input_list.append(x.strip())
		except:
			print "wrong inputfile"
			exit()
def get_word(words):
	output_word=words[0]
	words=words[1:]
	for i in words:
		if not output_word == '':
			if output_word[0]>i:
				output_word=output_word+i
			else:
				output_word=i+output_word
	return output_word



if __name__ == '__main__':
	#global digits
	get_input(sys.argv[1])
	T=int(input_list[0])
	testcases=input_list[1:]
	if (1 <= T) and (T<=100):
		index=1
		for testcase in testcases:
			print "Case #"+str(index)+": "+get_word(testcase)

			index=index+1

			
			
				
	else:
		print "testcases limit exceeded"