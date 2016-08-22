##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt0.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(s):
    end = ""
    if len(s) == 0:
        return end
    end = str(s[0])
    for c in s[1:]:
        if str(c) < str(end[0]):
            end += c
        else:
            end = c + end
    return end

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        s = input.readline().strip()
##        if case == 2:
        solution = solve(s)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        




main()
input.close()
output.close()
    
