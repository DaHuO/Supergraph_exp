t = int(raw_input())

for idx in range(1, t+1):
    stacks = [s for s in raw_input()]
    new_stacks = [stacks[0]]
    for s in stacks:
        if new_stacks[-1] != s:
            new_stacks.append(s)
    
    number_of_count = len([val for val in new_stacks if val == '-'])
    for i in range(len(new_stacks) -1):
        if new_stacks[i] == '+' and new_stacks[i + 1] == '-':
            number_of_count += 1
        
    print 'Case #{0}: {1}'.format(idx, number_of_count)
