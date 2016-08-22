import fileinput

cached = {
    '+': 0,
    '-': 1,
}

def test(value):
    end = len(value)
    result = 0
    while end > 0:
        if value[:end] in cached:
            result += cached[value[:end]]
            break
        last_char = value[end - 1]
        prev_char = value[end - 2]
        if last_char != prev_char and last_char == '-':
            result += 2
        end -= 1
    return result

def calculate(case, value):
    result = test(value)
    print "Case #{}: {}".format(case, result)

case = -1
for line in fileinput.input():
    case += 1
    if case < 1:
        continue
    calculate(case, line)
