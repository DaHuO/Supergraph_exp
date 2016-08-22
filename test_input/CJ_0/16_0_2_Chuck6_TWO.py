cases = int(input())
for i in range(cases):
    start = list(input())
    moves = 0
    for j in range(len(start)):
        current = len(start)-(j+1)
        #print(current)
        if(start[current] != '+'):
            for k in range(current):
                if(start[k] == "+"):
                    start[k] = "-"
                else:
                    start[k] = "+"
            moves += 1
        #print(start)
    print("Case #"+str(i+1)+": "+str(moves))