in_file = open("B-large.in","r")
T = in_file.readline()
T = int(T)
out_file = open("B-large.out","w")

for i in range(T):
    Stack = in_file.readline()
    Stack = Stack[0:len(Stack)-1]
    n_moves = 0
    index = len(Stack)-1
    
    while True:
        if Stack[index] == '+' and index >= 0:
            index = index - 1
        elif Stack[index] == '-' and index >= 0:
            n_moves = n_moves + 1
            f = ''
            for j in range(index+1):
                if Stack[j] == '+':
                    f = f + '-'
                else:
                    f = f + '+'
            Stack = f + Stack[index+1:len(Stack)]
        elif index < 0:
            break


    out_file.write("Case #"+str(i+1)+": "+str(n_moves)+"\n")
        
        
    









in_file.close()
out_file.close()
