
def flip_pancake(pancake):
    if pancake is '-':
        return '+'
    elif pancake is '+':
        return '-'

def flip_pancakes(pancake):
    stack = list(pancake)[::-1]
    flips = 0
    for i in range(0, len(stack)):
        if stack[i] == '-':
            flips += 1
            for j in range(i, len(stack)):
                stack[j] = flip_pancake(stack[j])
    return flips
    
instances = None
with open('input.txt', 'rU') as input:
    instances = input.readlines()

with open('output.txt', 'w') as output:
    case = 1
    for instance in instances[1:]:
        result = flip_pancakes(instance)
        output.write('Case #{}: {}\n'.format(case, result))
        case += 1
