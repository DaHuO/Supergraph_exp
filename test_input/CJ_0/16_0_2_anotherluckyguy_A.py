lines = open('input.txt').readlines()
lines.remove(lines[0])
output = open('out.txt', 'w')
lines = [i.strip() for i in lines]

a = 1
for it in lines:

    flips = 0
    p_state = None
    for state in it:
        if state == '-' and p_state is None:
            p_state = '-'
            flips += 1
        if state == '+' and p_state != '+':
            p_state = '+'
        if state == '-' and p_state == '+':
            p_state = '-'
            flips += 2
    print(flips)
    output.write('Case #{}: '.format(a) + str(flips))
    output.write('\n')
    a += 1
