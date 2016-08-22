
def solve(word):
    result = [word[0]]
    for w in word[1:]:
        if w >= result[0]:
            result.insert(0, w)
        else:
            result.append(w)
    
    return "".join(result)

    
def main(source, dest):

    with open(source, 'r') as fd, open(dest, 'w') as fo:
        T = int(fd.readline())
        for i in range(1,T+1):
            word = fd.readline().rstrip()
            result = solve(word)
	
            print 'Case #' + str(i) + ': ' + result + '\n',
            fo.write('Case #' + str(i) + ': ' + result + '\n')


if __name__ == "__main__":
	filename = os.path.basename(sys.argv[1])
	source = sys.argv[1]
	dest = os.path.join(sys.argv[2], filename.replace(".in.txt",".out.txt"))
	main(source, dest)