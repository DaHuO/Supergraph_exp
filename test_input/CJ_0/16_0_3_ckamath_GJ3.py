N = 15
J = 50

counter = 0
template = "1000000000000001"
halt = 0

for i in range(N-1,3,-1):
    for j in range(i-2,1,-1):
        current=list(template)
        current[i] = current[i-1] = current[j] = current[j-1] = "1"

        print ''.join(current), "3", "2", "3", "2", "7", "2", "3", "2", "3"

        counter += 1
        if counter == J:
            halt = 1
            break

    if halt == 1:
        break
