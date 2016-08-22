import sys

def happy(S):
    for s in S:
        if s == '-':
            return False
    return True

def findLastIndexMatching(S):
    for i in range(len(S)):
        if(S[i] != S[0]):
            return i-1
    return i

def reverse(subS):
    for i in range(len(subS)):
        if subS[i] == '-':
            subS[i] = '+'
        else:
            subS[i] = '-'
    subS = subS[::-1]

def flip(S,i):
    subS = S[0:i+1]
    reverse(subS)
    S[0:i+1] = subS

def maneuver(S):
    flips = 0
    while(not happy(S)):
        i = findLastIndexMatching(S)
        flip(S,i)
        flips+=1
    return flips

if __name__ == "__main__":
    f = open(sys.argv[1],'r')
    T = int(f.readline())
    for i in xrange(1,T+1):
        S = f.readline()
        minFlips = maneuver(list(S))
        print "Case #" + str(i) + ": " + str(minFlips)
    f.close()

