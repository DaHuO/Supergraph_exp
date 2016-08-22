f = open('A.in', 'r')
f_ans = open('A.out', 'w')

num_cases = int(f.readline())

def solve(S):
    curr_front = 64
    curr_str = ''
    for c in S:
        if ord(c) >= curr_front:
            curr_str = c + curr_str
            curr_front = ord(c)
        else:
            curr_str += c
    return curr_str


for i in range(num_cases):
    N = f.readline()
    ans = solve(N[:-1])
    f_ans.write("Case #" + str(i+1) + ": " + ans + '\n')
