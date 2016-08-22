v_dir = "k:\\Python\\codejam\\2016_Round1A_problem_a\\"
v_file_input = v_dir + "input_1.txt"
# filename = v_dir + "A-small-practice.in"
# filename = v_dir + "A-large-practice.in"

v_txt_in = open(v_file_input)
v_file_output = "output_1.txt"
v_txt_out = open(v_file_output, 'w')

v_number_of_tests = int(v_txt_in.readline())

v_test_number = 1

while v_test_number <= v_number_of_tests:
    v_string = v_txt_in.readline()

    v_result_string = ''
    for i in v_string:
        # print(v_result_string + i)
        # print(i + v_result_string)
        if v_result_string + i > i + v_result_string:
            v_result_string = v_result_string + i
        else:
            v_result_string = i + v_result_string

    # v_txt_out.write("Case #" + str(v_test_number) + ": " + v_result_string + "\n")
    v_txt_out.write("Case #" + str(v_test_number) + ": " + v_result_string)     # my v_result_string ALREADY have \n !!!
    v_test_number += 1

