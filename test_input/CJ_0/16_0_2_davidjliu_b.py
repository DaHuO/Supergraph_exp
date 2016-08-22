


inputs = int(raw_input())

for i in range(inputs):
    cakes = raw_input()

    curr_on = cakes[0]
    count = 0
    
    for j in cakes[1:]:
        if j != curr_on:
            count += 1
        curr_on = j
    if curr_on == "-":
        count += 1
        
    print "Case #" + str(i+1) + ": " + str(count)
    
    
