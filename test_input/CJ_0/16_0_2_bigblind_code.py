import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out
tc = 0

class ImpossibleError(Exception):
	pass

t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out


for tc in xrange(t):
    swaps = 0
    stack = inp.readline().strip() + "+"
    for i in xrange(len(stack)-1):
        if stack[i] != stack[i+1]:
            swaps += 1
    print_case(tc+1, swaps)
	