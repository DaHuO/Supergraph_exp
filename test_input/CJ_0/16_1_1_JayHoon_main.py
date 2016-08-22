__author__ = 'jaehoonlee88'

input_file = open('A-large.in', "r")
output_file = open('output.txt', "w")

T = int(input_file.readline())

for i in range(0, T):
    input_str = input_file.readline().rstrip('\n')

    firstlet = ''
    bigword = ''

    for ch in list(input_str):

        if firstlet == '':
            firstlet = ch
            bigword = ch
        else:
            if firstlet <= ch:
                bigword = ch + bigword
                firstlet = ch
            else :
                bigword = bigword + ch



    output_file.write("Case #" + str(i+1) + ": " + bigword + '\n')
    #print bigword

input_file.close()
output_file.close()







