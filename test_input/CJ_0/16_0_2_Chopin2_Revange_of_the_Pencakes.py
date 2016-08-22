import sys

def reading_the_file(input_file):
    f = open(input_file, 'r+')
    return f

def getting_test_cases(f):
    y0 = []
    for counter, line in enumerate(f):
        case = counter + 1
        if counter == 0:
            number_of_test_cases = line
            continue
        if counter > 0:
            y0.append(line[:-1])
    return {'C': y0, 'cases' : int(number_of_test_cases) }

def going_through_the_cases(C,cases):
    output_file_name = sys.argv[1][:-2]+'out'
    with open(output_file_name, 'w') as f:
        for i in range(cases):
            result = algorithm(C[i])
            f.write('Case #{}'.format(i+1)+': '+ str(result) + '\n')


def getting_the_stack(whole_stack, count):
    if bool('-' in set(whole_stack)) == False:
        return { 'stack': new_stack, 'count': count }
    for counter, pencake in enumerate(whole_stack):
        if whole_stack[-counter-1] == '-':
            bottom = len(whole_stack)-counter
            new_stack = whole_stack[:bottom]
            return { 'stack': new_stack, 'count': count }
    
def flipping_top(stack, count):
    last_plus = 0
    '''Turning the +s on 
    the top'''
    if stack[0] == '-':
        return { 'stack': stack, 'count': count }
    else:
        while stack[last_plus] == '+':
            last_plus += 1
        new_stack = '-'*last_plus + ''.join(stack[last_plus:])
        count += 1
        return { 'stack': new_stack, 'count': count }

def flipping_the_stack(stack, count):
    count += 1
    list_stack = list(stack)
    new_stack = []
    for i in range(len(stack)):
        if list_stack[i]=='-':
            list_stack[i]='+'
        else:
            list_stack[i]='-'
    for j in range(len(list_stack)):
        new_stack.append(list_stack[-j-1])
    return { 'stack': new_stack, 'count': count }

def algorithm(stack):
    count = 0
    if bool('-' in set(stack)) == False:
        return 0
    while bool('-' in set(stack)) == True:
        result = flipping_the_stack(**flipping_top(**getting_the_stack(stack, count)))
        stack = result['stack']
        count = result['count']
    return result['count']

def main():
    input_file = sys.argv[1]
    going_through_the_cases(**getting_test_cases(reading_the_file(input_file)))

if __name__ == '__main__':
    main()

