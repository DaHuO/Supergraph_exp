fileout = open('A-large.out',"w")

with open('A-large.in') as file:
    T = int(file.readline())
    
    for case in range(1, T+1): 
        S = list(file.readline().strip())
        newS = S[0]
        for i in range(1, len(S)):
            
            if S[i] >= newS[0]:
                newS = S[i]+ newS
            else:
                newS = newS + S[i]
        fileout.write("Case #" + str(case) + ": " + str(newS) + "\n")
    
fileout.close()
