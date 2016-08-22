def sum_in_base(prod, base):
    tot = 0
    for st in range(1, len(prod) + 1):
        if prod[-1 * st] == '1':
            tot += base ** st
    return tot


'''
#################
# SMALL DATASET #
#################

out = open('coinjamsmall.out', 'w')
out.write('Case #1:\n')

good = 0
cc = 1
while good < 50:
    line = bin(cc)[2:]
    cc += 1
    rt = ['1' + ('0' * (16 - 2 - len(line))) + line + '1']
    two = sum_in_base(line, 2)
    if any(sum_in_base(line, j) % 2 != 0 for j in range(3, 10, 2)):
        continue
    if two % 3 == 0:
        rt.append('3')
    elif two % 11 == 0:
        rt.append('11')
    else:
        continue
    rt.append('2')
    four = sum_in_base(line, 4)
    if four % 5 == 0:
        rt.append('5')
    elif four % 13 == 0:
        rt.append('13')
    else:
        continue
    rt.append('2')
    six = sum_in_base(line, 6)
    if six % 7 == 0:
        rt.append('7')
    elif six % 11 == 0:
        rt.append('11')
    else:
        continue
    rt.append('2')
    eight = sum_in_base(line, 8)
    if eight % 3 == 0:
        rt.append('3')
    elif eight % 11 == 0:
        rt.append('11')
    else:
        continue
    rt.append('2')
    ten = sum_in_base(line, 10)
    if ten % 7 == 0:
        rt.append('7')
    elif ten % 11 == 0:
        rt.append('11')
    else:
        continue
    good += 1
    out.write(' '.join(rt) + '\n')

out.close()
'''

#################
# LARGE DATASET #
#################

out = open('coinjamlarge.out', 'w')
out.write('Case #1:\n')

good = 0
cc = 1
while good < 500:
    line = bin(cc)[2:]
    cc += 1
    rt = ['1' + ('0' * (32 - 2 - len(line))) + line + '1']
    two = sum_in_base(line, 2)
    if any(sum_in_base(line, j) % 2 != 0 for j in range(3, 10, 2)):
        continue
    if two % 3 == 0:
        rt.append('3')
    else:
        continue
    rt.append('2')
    four = sum_in_base(line, 4)
    if four % 5 == 0:
        rt.append('5')
    else:
        continue
    rt.append('2')
    six = sum_in_base(line, 6)
    if six % 7 == 0:
        rt.append('7')
    else:
        continue
    rt.append('2')
    eight = sum_in_base(line, 8)
    if eight % 3 == 0:
        rt.append('3')
    else:
        continue
    rt.append('2')
    ten = sum_in_base(line, 10)
    if ten % 11 == 0:
        rt.append('11')
    else:
        continue
    good += 1
    out.write(' '.join(rt) + '\n')

out.close()
