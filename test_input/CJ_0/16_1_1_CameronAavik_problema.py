problem = 'A'
sol_set = 'large'


def solve(line):
    string = ''
    for char in line:
        if string == '':
            string = string + char
            continue
        first_code = ord(string[0])
        char_code = ord(char)
        if first_code > char_code:
            string = string + char
        else:
            string = char + string
    return string

if sol_set == 'test':
    filename = 'input.txt'
elif sol_set == 'small':
    filename = problem + '-small-attempt0.in'
else:
    filename = problem + '-large.in'
file = open(filename, 'r')
out_file = open('output_file.txt', 'w')
amount = file.readline()
for i in range(int(amount)):
    line_read = file.readline().strip()
    output = solve(line_read)
    out_file.write("Case #" + str(i + 1) + ": " + output + "\n")

file.close()
out_file.close()
