import sys
d = {'11':'1', '1i':'i', '1j':'j', '1k':'k', 'i1':'i',  'ii':'-1' ,  'ij':'k',  'ik':'-j', \
'j1':'j',  'ji':'-k' ,  'jj':'-1', 'jk':'i', 'k1':'k',  'ki':'j'  ,  'kj':'-i', 'kk':'-1' }

def evaluate(t1, t2):
	neg1, neg2 = t1.count('-') , t2.count('-')
	t1, t2 = t1.replace('-',''), t2.replace('-','')
	neg = neg1 + neg2
	key = t1 + t2
	result = d[key]
	if (neg % 2) == 1:
		if result[0] == '-':
			result = result[1:]
		else:
			result = '-' + result
	return result


def evaluate_substring(substr):
	result = substr[0]
	if result == 'i':
		Bool_i = True
	Bool_i, Bool_ij = False, False
	for i in xrange(1, len(substr)):
		result = evaluate(result, substr[i])
		if result == 'i' and Bool_i == False:
			Bool_i = True
		if result == 'k' and Bool_i == True:
			Bool_ij = True
	if result == '-1' and Bool_ij == True:
		return True
	return False




def main():
	file_name = 'C-small-attempt0.in'
	fh = open(file_name, 'rt')
	line = fh.readline()
	test_cases = int(line)
	Res = ''
	for i in xrange(1, test_cases+ 1):
		line1 = fh.readline().replace('\n','') 
		line2 = fh.readline().replace('\n','')
		Iter = int(line1.split(' ')[1])
		string = str(line2) * Iter
		if len(string) < 3:
			Res += 'Case #' + str(i) + ": NO\n"
			continue
		elif len(string) == 3:
			if string == 'ijk':
				Res += 'Case #' + str(i ) + ": YES\n"
                        	continue
			else:
				Res += 'Case #' + str(i ) + ": NO\n"
                        	continue
		eval_str = evaluate_substring(string)
		if eval_str == True:
			Res += 'Case #' + str( i ) + ": YES\n"
		else:
			Res += 'Case #' + str(i ) + ": NO\n"
	fh.close()
	f = open('saber_dijkstra.out', 'w')
	f.write(Res)
	f.close()

main()
