T = int(raw_input())
for case in range(T):
    cakes = raw_input().strip()
    if cakes.find("-") == -1: # All are happy side
        print "Case #{}: {}".format(case+1, 0)
    elif cakes.find("+") == -1: # All are blank side
        print "Case #{}: {}".format(case+1, 1)
    else:
        total_switch = 0
        current_face = cakes[0]
        pos = 1
        while pos < len(cakes):
            if cakes[pos] != current_face:
                total_switch+=1
                current_face = "-" if current_face == "+" else "+"
            pos+=1
        if current_face == "-": # Final switch was all with down side
            total_switch += 1
        print "Case #{}: {}".format(case+1, total_switch)




