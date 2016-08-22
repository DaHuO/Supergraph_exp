import sys

test_file = open(sys.argv[1], 'r')
test = test_file.read().split('\n')
test_file.close()

total = int(test[0])

output = ""

for i in range(total):
    count = 0
    flipped_pancakes = list(test[i + 1])
    length = len(flipped_pancakes)
    pancakes = []
    for j in range(length):
        pancakes.append(flipped_pancakes[length - j - 1])
    
    count = 0

    for j in range(length):
        if pancakes[j] == '-':
            count = count + 1
            copy = pancakes
            for k in range(length - j):
                if copy[k + j] == '-':
                    pancakes[k + j] = '+'
                else:
                    pancakes[k + j] = '-'
    output = output + 'Case #' + str(i + 1) + ': ' + str(count) + '\n'

print output

output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()