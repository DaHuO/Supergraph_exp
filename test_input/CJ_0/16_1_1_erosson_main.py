# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
import sys
import logging
#logging.basicConfig(level=logging.DEBUG) # debug, info, warning, error, critical, exception
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def run(chars):
    ret = chars[0]
    for c in chars[1:]:
        # prepend later letters, append others
        if ret[0] <= c:
            ret = c + ret
        else:
            ret = ret + c
    log.debug('%s -> %s', chars, ret)
    return ret

def parse(lines):
    return lines.pop(0).strip()
    #(a, b) = (int(x) for x in lines.pop(0).split())
    #return dict(a=a, b=b)

def main(infile):
    lines = infile.readlines()
    count = int(lines.pop(0))
    cases = (parse(lines) for case in range(count))
    #output = (run(**case) for case in cases)
    output = (run(case) for case in cases)
    for i, result in enumerate(output):
        print "Case #%d: %s" % (i + 1, result)

if __name__=='__main__':
    main(sys.stdin)
