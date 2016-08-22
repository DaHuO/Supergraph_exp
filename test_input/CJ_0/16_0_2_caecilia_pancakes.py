T = int(input())


for t in range(T):
    actions = 0
    s = input().strip()
    goal = '+'
    for c in reversed(s):
        #print(c, goal, actions)
        if c != goal:
            actions += 1
            goal = '+' if goal == '-' else '-'
    print("Case #%s:" %(t+1), actions)
            
