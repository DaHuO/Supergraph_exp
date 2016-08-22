def LastWord(word):
    n=0
    res=word[0]
    for single in word:
        if n==0:
            n = 1
            continue
        if res[0]>single:
            res=res+single
        else:
            res=single+res
    return res


if __name__ == "__main__":
	fopen=open('test.in')
	output=open('output.txt', 'a')
	line_number=0
	for lines in fopen:
		if(line_number==0):
			line_number=line_number+1
			continue
		word=lines.strip()
		output.write('Case #'+str(line_number)+': ')
		output.write(LastWord(word)+'\n')
		line_number = line_number + 1
	output.close()
