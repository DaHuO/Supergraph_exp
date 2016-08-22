import sys;

def solveAndPrint(t):
    S = sys.stdin.readline();
    lastWord = S[0]
    for c in S[1:]:
        if c >= lastWord[0]:
            lastWord = c + lastWord
        else:
            lastWord = lastWord + c
    print ('Case #' + str(t) + ': ' + lastWord, end='')

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        solveAndPrint(i+1);

main()
