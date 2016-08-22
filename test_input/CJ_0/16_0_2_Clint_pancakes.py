#import heapq

def pancakes(stack):
    stack.reverse()
    flips = 0
    previous = stack.pop()
    while len(stack) > 0:
        flips += stack[-1] != previous
        previous = stack.pop()
    
    flips += previous == '-'
    return flips
        
if __name__ == '__main__':
    for T in range(int(raw_input())):
        stack = [c for c in raw_input().strip()]
        print "Case #%d: %d" % (T+1, pancakes(stack))