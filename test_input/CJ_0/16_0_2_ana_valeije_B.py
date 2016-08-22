import sys	

def clean_seq(seq):
	new_seq = seq[0]
	for item in seq[1:]:
		if item != new_seq[-1]:
			new_seq += item
	if new_seq[-1] == '+':
		new_seq = new_seq[:-1]
	return new_seq
	
def solveCase(case, f, fout):
	seq = f.readline().strip()
	seq = clean_seq(seq)
	result = len(seq)
	writeLine(fout, case, str(result))

def writeLine(fout, n, result):
	print("Case #%d: %s\n" %(n, result))
	fout.write("Case #%d: %s\n" %(n, result))

if __name__ == '__main__':
	
	inputFileName = sys.argv[1]
	
	f = file(inputFileName)
	fout = file("%s.out" %(inputFileName.split(".")[0]), "w")
	
	T = eval(f.readline())
	
	for case in xrange(T):
		solveCase(case + 1, f, fout)
		
	f.close()
	fout.close()
