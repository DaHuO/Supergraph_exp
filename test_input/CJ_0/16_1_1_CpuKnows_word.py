g = open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\Last Word\word_small_out.txt','w+')

with open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\Last Word\word_sample.txt', 'r+') as f:
    num_cases = int(f.readline())
    
    for i in range(num_cases):
        S = f.readline()
        S = list(S)
        
        S_out = []
        for j in S:
            if(len(S_out) == 0):
                S_out.append(j)
            elif(j < S_out[0]):
                S_out.append(j)
            else:
                S_out.insert(0, j)
                
        S_out = ''.join(S_out)
        
        g.write('Case #' + str(i+1) + ': ' + S_out)
        
g.close()