import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        S = line.rstrip("\n\r")
        instances.append(S)
        logging.debug ("Instance: %s" % S)
    line_no+=1

def instance(inst):
    result = ""
    for x in inst:
        logging.debug (x)
        if len(result) > 0:
            if result[0] > x:
                result += x
            else:
                result = x + result
        else:
            result = x
    return result
            
out_line_no = 1
for x in instances:
    result = instance(x)
    if isinstance(result,str):
        print "Case #%d: %s" % (out_line_no, instance(x))
    else:
        print "Case #%d: %d" % (out_line_no, instance(x))
    out_line_no+=1


