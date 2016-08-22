def pancake(stack):
    if '+' not in stack:
        return 1
    
    count = 0 if stack[0] == '+' else 1
    stack = stack.lstrip('-').rstrip('+')
    
    while len(stack) != 0:
        stack = stack.lstrip('+').lstrip('-')
        count += 2

    return count

def Solution():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        stack = raw_input()  # Every character in stack is either + or -.
        res = pancake(stack)
        print "Case #{}: {}".format(i, res)

if __name__ == "__main__":
    Solution()