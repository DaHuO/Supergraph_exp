import csv

INPUT_FILE = "./B-large.in"
OUTPUT_FILE = "B-large-output.csv"

file_inputs = [line.rstrip('\n') for line in open(INPUT_FILE)]

results = []


case = 1

for file_input in file_inputs[1:]:

    starting_stack = file_input
    previous_char = starting_stack[0]
    flips = 0

    for char in starting_stack[1:]:
        if char == previous_char:
            pass
        else:
            flips += 1
            previous_char = char

    if starting_stack[-1] == "-":
        flips += 1

    results.append(["Case #" + str(case) + ": " + str(flips)])
    case += 1



resultFile = open(OUTPUT_FILE, 'w')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(results)
resultFile.close()