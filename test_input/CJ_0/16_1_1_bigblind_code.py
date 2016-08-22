import sys, math
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    print "Case #%d: %s" % (case, str(result))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

for tc in xrange(t):
    word = inp.readline().strip()
    result = word[0]
    
    for c in word[1:]:
        if c < result[0]:
            result = result + c
        else:
            result = c + result
    
    print_case(tc+1, result)