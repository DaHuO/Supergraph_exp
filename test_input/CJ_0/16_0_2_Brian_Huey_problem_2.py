def convertStack(inpstr):
    stack = inpstr.replace('-', '0')
    stack = stack.replace('+', '1')
    stack = [int(i) for i in stack]
    return stack

def scoreStack(inpstr, case):
    stack = convertStack(inpstr)
    moves = 0
    zeroes = False
    if stack == [1 for i in range(len(stack))]:
        return 'Case #%s: 0\n' % (case)
    if stack == [0 for i in range(len(stack))]:
        return 'Case #%s: 1\n' % (case)
    for idx, i in enumerate(stack):
        if idx < 1:
            continue
        elif (stack[idx-1:idx+1] == [0, 1]) & zeroes:
            moves += 2
            zeroes = False
        elif stack[idx-1:idx+1] == [0, 1]:
            moves += 1
        elif stack[idx-1:idx+1] == [1, 0]:
            zeroes = True
    if zeroes:
        moves += 2
    return 'Case #%s: %s\n' % (case, str(moves))


inputFile = 'B-large.in'
outputFile = 'B-large.out'
out = []
for idx, row in enumerate(open(inputFile, 'r')):
    if idx == 0:
        T = row
    else:
        case = str(idx)
        out.append(scoreStack(row.strip(), case))
open(outputFile, 'wa').writelines(out)