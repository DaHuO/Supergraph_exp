inputF = open('B-large.in', 'r')
output = open('B-large.out', 'w')

numCases = int(inputF.readline())

for i in range(numCases):
    line = inputF.readline()
    line = line[:-1] + '+'
    switchCount = 0
    for j in range(len(line)-1):
        if line[j] != line[j+1]:
            switchCount += 1
    
    output.write('Case #' + str(i+1) + ': ')
    output.write(str(switchCount) + '\n')

inputF.close()
output.close()
