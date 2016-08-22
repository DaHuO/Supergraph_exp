_name = "A-large"
# Load the file in a list
with open("{}.in".format(_name)) as f:
    data_set = [line.rstrip() for line in f]

# Remove the first entry since we don't really need it.
no_of_tests = data_set.pop(0)
current_test_no = 1

for n in data_set:
    first_letter = ""
    last_letter = ""
    last_word = []

    for i in n:
        if last_word == []:
            last_word.append(i)
            first_letter = i
            continue

        if ord(i) >= ord(first_letter):
            first_letter = i
            last_word.insert(0, i)
        else:
            last_word.append(i)

    last_word = ''.join(last_word)
    print last_word
    
    with open("{}.out".format(_name), 'a') as f:
        f.write("Case #{0}: {1}\n".format(current_test_no, last_word))

    current_test_no += 1
