import sys


def do(S):
    out = [S[0]]
    S = S[1:]

    for s in S:
       if s<out[0]:
          out.append(s)
       else:
          out.insert(0,s)
    return ''.join(out)



T = int(sys.stdin.readline())
for t in range(T):
    S = sys.stdin.readline().strip()
    print "Case #%i:"%(t+1), do(S)
