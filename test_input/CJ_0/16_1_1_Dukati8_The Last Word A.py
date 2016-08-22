import sys
sys.setrecursionlimit(2000)
def recurbestword(S):
    if len(S)<=1:
        return S
    else:

        maxChar=S[-1]
        maxindex=len(S)-1
        for i in range (len(S)-1,-1,-1):
            if S[i]>maxChar:
                maxChar=S[i]
                maxindex=i

        return (maxChar+recurbestword(S[:maxindex])+S[maxindex+1:])

T=int(input())
for i in range (T):
    S=input()
    best=recurbestword(S)
    print ("Case #" + str(i+1) + ": " + best)
