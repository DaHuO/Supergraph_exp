def flip(bits, k):
    bits [:k] = map(lambda x: not x, bits[:k])
    return bits

def getFlips(stack):
    if all(stack):
        return 0
    else:
        return 1 + getFlips(flip(stack, len(stack)-stack[::-1].index(False)))
        
    
t = int(input())

for c in range(t):
    cStack = list(map(lambda x: x == '+', input()))
    print("Case #" + str(c+1) + ": " + str(getFlips(cStack)))