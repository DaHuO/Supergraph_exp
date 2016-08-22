SAD = '-'

def min_flips(stack):
    nb_changes = 0
    for i in range(0,len(stack)-1):
        if stack[i] != stack[i+1]:
            nb_changes += 1

    if stack[-1] == SAD:
        return 1 + nb_changes
    else:
        return nb_changes

f_in = open('input.txt', 'r')
f_out = open('output.txt', 'w')

nb_tests = int(f_in.readline())
for i in range(1, nb_tests+1):
    stack = f_in.readline().rstrip('\n')
    _min = min_flips(stack)
    f_out.write('Case #{}: {}'.format(i, _min))
    f_out.write('\n')

