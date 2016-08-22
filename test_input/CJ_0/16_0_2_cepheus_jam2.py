import sys


def start():
    T = sys.stdin.readline()
    # T=1
    case = 0
    for i in xrange(int(T)):
        case += 1
        line = sys.stdin.readline()
        
        
        line = line.strip()
        score = 1 if line[0]=='-' else 0

        past = line[0]

        for sign in line[1:]:
            if not sign == past:
                if past == '+':
                    score += 2

                past = sign


        print "Case #%s: %s" % (case, score)

if __name__ == "__main__":
    start()