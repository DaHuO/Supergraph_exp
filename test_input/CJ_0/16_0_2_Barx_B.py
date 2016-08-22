def solve(stack):
	count = 1 if stack[-1] == '-' else 0
	current = stack[0]
	for c in stack[1:]:
	    if c != current:
	    	count += 1
	    	current = c
	return str(count)

def main(source, dest):
    with open(source, 'r') as fd, open(dest, 'w')as fo:
        T = int(fd.readline())
        for i in range(1,T+1):
			stack = fd.readline().rstrip()
			result = solve(stack)
			print 'Case #' + str(i) + ': ' + result
			fo.write('Case #' + str(i) + ': ' + result + '\n')

if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)