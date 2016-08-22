import os

def maneuver(sequence, move=0):
    if len(filter(lambda x:not x, sequence))==0:
        return move
    else:
        pos = 0
        if sequence[pos]:
            while sequence[pos]:
                pos += 1
            print sequence, pos
            return maneuver([False]*(pos+1) + sequence[(pos+1):], move=move+1)
        else:
            while (not sequence[pos]) and pos < len(sequence)-1:
                pos += 1
            print sequence, pos
            return maneuver([True]*(pos+1) + sequence[(pos+1):], move=move+1)

inf = open('input.in','r')
inp = inf.read().split('\n')
inf.close()
outf = open('output','w')
T = int(inp.pop(0))
for i in range(T):
    S = [x=='+' for x in inp.pop(0)]
    outf.write('Case #%d: %d\n'%(i+1, maneuver(S)))
outf.close()
