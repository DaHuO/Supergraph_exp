import time
import datetime
__author__ = 'eegee'

filename = "A-large"

input_data = open("../data/" + filename + ".in")
output_data = open("../data/" + filename + ".out", "w")
time.perf_counter()

for case in range(int(input_data.readline())):
    # read inputs #
    letters = list(input_data.readline().rstrip())
    # read inputs #

    answer = ""
    # solution #
    for letter in letters:
        if answer and ord(answer[0]) > ord(letter):
            answer = answer + letter
        else:
            answer = letter + answer
    # solution #

    # display and write output #
    output_line = "Case #" + str(case + 1) + ": "
    print(output_line + str(answer))
    output_data.write(output_line + str(answer) + "\n")
    # display and write output #

print()
print("total_time:", datetime.timedelta(seconds=time.perf_counter()))
input_data.close()
output_data.close()
