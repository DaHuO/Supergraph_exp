"""
Fernando Gonzalez del Cueto
Google Code Jam Round 1a-- Apr 13, 2016

Problem A
"""

from codejam import Problem


input_file = 'A-large.in'
prob = Problem(input_file)

def myfun(stream):

    s = stream[0]
    for c in stream[1:]:

        s1 = s+c
        s2 = c+s

        if s1>s2:
            s = s1
        else:
            s = s2

    return s


n_cases = prob.parse_int()
for case_j in range(1, n_cases+1):

    #fid_in = prob.f_in

    stream = prob.readline()
    # print(case_j, l)

    out_line = myfun(stream)
    prob.write(case_j, out_line, print_out=True)

# close input and output files
prob.close()