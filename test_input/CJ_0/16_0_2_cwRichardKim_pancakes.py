num_cases = int(raw_input())

for case_num in range(num_cases):
        p_stack = raw_input()
        count = 1
        current = p_stack[0]
        for p in p_stack:
                if p != current:
                        count += 1
                        current = p
        if current == "+":
                count -= 1
        print ("Case #%i: %i" % (case_num+1, count))
