o = open("C:\Users\ANTON\Downloads\A-large.in")
w = open("C:\Users\ANTON\PycharmProjects\CodeJam\Round1A\TheLastWord\Large-Output.txt", 'w')

input_lines = [i.strip('\n') for i in o]

cases = input_lines.pop(0)

for index, word in enumerate(input_lines):
    solution = word[0]
    for letter in word[1:]:
        if ord(letter) >= ord(solution[0]):
            solution = letter + solution
        else:
            solution += letter

    w.write("Case #" + str(index + 1) + ": " + solution + '\n')
