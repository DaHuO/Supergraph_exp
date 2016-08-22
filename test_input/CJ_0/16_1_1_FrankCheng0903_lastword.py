file_strings = []
with open("lastword.txt") as data_file:
    for line in data_file:
        file_strings.append(line.strip())
test_case_number = file_strings[0]
file_strings.pop(0)

case = 1
for word in file_strings:
    final_word = ""
    final_word += word[0]
    for i in range(1, len(word)):
        if word[i] >= final_word[0]:
            final_word = word[i] + final_word
        else:
            final_word += word[i]
    print("Case #{}: {}".format(case, final_word))
    case += 1
