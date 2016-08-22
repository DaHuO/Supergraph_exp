

def solve_case(s):
    best_letter = s[0]
    
    r = s[0]
    
    for x in s[1:]:
        if x >= best_letter:
            best_letter = x
            r = x + r
        else:
            r+=x
            
    return r

num_cases = input()
cur_case = 1

while cur_case <= num_cases:
    print "Case #"+str(cur_case)+": "+solve_case(raw_input())
    cur_case += 1