def process_word(s):
	result = s[0]
	for ch in s[1:]:
		if ch<result[0]:
			result+=ch
		else:
			result = ch+result
	return result


num = input()
outs = []
for i in xrange(num):
	outs.append("Case #%d: %s"%(i+1,process_word(raw_input())))
print '\n'.join(outs)

def output():
	f = open("out.txt",'w')
	f.write('\n'.join(outs))
	f.close()

#output()