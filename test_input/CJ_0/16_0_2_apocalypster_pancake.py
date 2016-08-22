def flip(stack,i):
    # 0 up till i are same
    if stack[0] == '+':
        return '-'*(i+1) + stack[i+1:]
    else:
        return '+'*(i+1) + stack[i+1:]

f = open("pancake.in",'r')
g = open("pancake_output.txt", 'w')
T = int(f.readline().strip())
for lol in range(1,T+1):
    stack = f.readline().strip()
    flips = 0
    while '-' in stack:
        i = 0
        while i < len(stack)-1 and stack[i] == stack[i+1]:
            i += 1

        stack = flip(stack,i)
        flips += 1
        
    g.write("Case #" + str(lol) + ": " + str(flips) + '\n')

f.close()
g.close()

    
