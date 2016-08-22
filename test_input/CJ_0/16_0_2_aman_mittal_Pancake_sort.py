f = open('B-large.in', 'r')
output = open('output.txt', 'w')


def flip(s):
    return s.replace('+', '.').replace('-', '+').replace('.', '-')[::-1]
T = int(f.readline().strip())
for x in range(T):
    count = 0
    ini_order = f.readline().strip()
    while ini_order.find('-') != -1:
        right_pointer = ini_order.rfind('-')
        left_pointer = ini_order.find('-')
        if left_pointer != 0:
            ini_order = ini_order[:left_pointer].replace('+', '-') + ini_order[left_pointer:]
            count += 1
        ini_order = flip(ini_order[:right_pointer+1]) + ini_order[right_pointer+1:]
        count += 1
    output.write('Case #{0}: {1}\n'.format(x+1, count))
f.close()
output.close()
