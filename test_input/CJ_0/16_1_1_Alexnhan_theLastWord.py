import sys

def makeLastWord(S):
    A = list(S)
    B = []
    for i in range(len(A)-1):
        if len(B) > 0 and A[i] >= B[0]:
            B[1:] = B[0:]
            B[0] = A[i]
        else:
            B.append(A[i])
    return ''.join(B)

if __name__ == "__main__":
    f = open(sys.argv[1],'r')
    T = int(f.readline())
    for i in range(1,T+1):
        S = makeLastWord(f.readline())
        print "Case #" + str(i) + ": " + S
    f.close()
