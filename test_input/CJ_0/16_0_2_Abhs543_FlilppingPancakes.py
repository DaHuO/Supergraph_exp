def flip(pancakes, n):
    myString=pancakes[0:n]
    reversedPancakes=myString[::-1]
    result=""
    for c in reversedPancakes:
        if c=="+":
            result+="-"
        else:
            result+="+"
    return result+pancakes[n:]

def solve(pancakes):
    count=0
    for i in xrange(len(pancakes)-1):
        if pancakes[i]!=pancakes[i+1]:
            count+=1
            pancakes=flip(pancakes, i+1)
    if pancakes[0]=="-":
      count+=1
      pancakes=flip(pancakes, len(pancakes))
    return count
            

if __name__ == "__main__":
	testcases = input()
	 
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		print("Case #%i: %s" % (caseNr, solve(cipher)))
