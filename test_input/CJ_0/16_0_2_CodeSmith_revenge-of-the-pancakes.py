# Problem B. Revenge of the Pancakes

def run():
	i = 0
	with open('input.txt', 'rt') as src, open('output.txt', 'wt') as tgt:
		for line in src:
			line = line.rstrip('\r\n')
			if i > 0:
				print "Case #%d: %d" % (i, processItem(i, line))
				tgt.write("Case #%d: %d\n" % (i, processItem(i, line)))
			i = i + 1


def processItem(lineNo, item):
	if (len(item) == 1 and item == '+') or not ('-' in item):
		return 0
	elif len(item) == 1 and item == '-':
		return 1
	else:
		cnt = 0
		while '-' in item:
			c = item[0]
			i = 0
			while item[i] == c and i < len(item) - 1:
				i = i + 1
			j = 0
			if c == '+':
				c = '-'
			else:
				c = '+'
			while j <= i:
				item = item[0:j] + c + item[j+1:]
				j = j + 1
			cnt = cnt + 1 
		return cnt
			

run()