
def flip(s):
    res = ''
    for i in range(0, len(s)):
        if s[i] == '+':
            res += '-'
        else:
            res += '+'
    return res

def canFlip(pancakes, ctr, L):
    global visited
    if pancakes in visited and visited[pancakes] <= ctr:
        return False
    visited[pancakes] = ctr
    # print('pancakes: {0}, ctr: {1}'.format(pancakes, ctr))
    if pancakes == '+' * len(pancakes):
        return True
    if ctr >= L:
        return False
    for i in range(0, len(pancakes)):
        result = flip(pancakes[0:(i+1)][::-1]) + pancakes[i+1:]
        # print('   if flip at {0} becomes {1}'.format(i, result))
        can_flip = canFlip(result, ctr+1, L)
        if can_flip:
            return True
    return False

T = int(input())


for t in range(0, T):
    global visited
    S = input()
    for depth_limit in range(0, 2 * len(S) + 1):
        
        visited = {}
        can_flip = canFlip(S, 0, depth_limit)
        if can_flip:
            print('Case #{0}: {1}'.format(t + 1, depth_limit))
            break;


