fh = open("input", "r")
data = []
fh.next()
for line in fh:
    data.append(line.strip())

print data

def invert(s):
    inv = ""
    for c in s:
        if c == "-":
            inv += "+"
        else:
            inv += "-"
    return inv

fw = open("output", "w")
case = 1

for prob in data:
    print 
    print "NEW PROBLEM"
    print prob
    manip = prob
    target = "+"*len(prob)
    
    flips = 0
    while manip != target:
        print("start while")
        pos = manip.rfind("-") + 1
        print "pos of last -: %s" %pos
        print "manip up till this position: %s" %manip[:pos]

        inverted = invert(manip[:pos])
        print "inverted: %s" %inverted
        manip = inverted + manip[pos:]
        flips += 1
        print "Manip is now: %s" %manip
    print "SOLVED"
    print "flips: %s " %flips
    fw.write("Case #%s: %s\n" %(case, flips))
    case += 1

