
def is_first(arr, current, first):

    n = len(arr)
    current_index = 0
    first_index = 0
    for index in xrange(n):
        if arr[index] == current:
            current_index = index

        if arr[index] == first:
            first_index = index

    # print current_index, first_index
    if current_index > first_index:
        return False

    return True

input_lines = []
output_lines = []

with open('input.txt', 'r') as input:
    data = input.read()

input_lines = data.split('\n')


case = 0
for a_input in input_lines[1:]:
    case += 1

    n = len(a_input)
    if n == 1:
        value = a_input

    else:

        sorted_input =  sorted(set(a_input), reverse=True)
        # print sorted_input
        S = a_input[0]
        word = S

        for index in xrange(1, n):
            # print word
            c = a_input[index]
            if is_first(sorted_input, c, word[0]):
                word = c + word
            else:
                word = word + c
        value = word


    output_lines.append('Case #%s: %s' % (case, value))

data = '\n'.join(output_lines)
with open('output.txt', 'w') as output:
    output.write(data)

