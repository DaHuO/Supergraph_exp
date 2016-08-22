#Pancake madness
def FlipsRequired(stack):
    numFlips = 0
    
    if len(stack) == 0:
        return 0
    
    prev = stack[len(stack)-1]
    
    if prev == '-':
        numFlips += 1
        
    for i in range(len(stack)-1, -1, -1):
        if prev != stack[i]:
            numFlips += 1
            prev = stack[i]

    return numFlips

def main():
    f = open('pancake.in', 'r')
    numCases = int(f.readline())

    for i in range(1, numCases+1):
        stack = list(f.readline().strip())
        print('Case #', i, ': ', FlipsRequired(stack), sep='')

main()
