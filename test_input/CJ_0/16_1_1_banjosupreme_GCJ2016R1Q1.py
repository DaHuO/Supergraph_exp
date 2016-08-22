def CJR1Q1(fname):
    
    infile = open(fname, 'r')
    outfile = open(fname+'out', 'w')
    
    from csv import reader
    
    myReader = reader(infile, delimiter = ' ')
    
    for row in myReader:
        cases = int(row[0])
        break
        
    j = 0
    for row in myReader:
        if j >= cases:
            break
        input = row[0]
        output = input[0]
        start = input[0]
        for k in range(1,len(input)):
            if input[k] >= start:
                output = input[k]+output
                start = input[k]
            else:
                output = output + input[k]
        j+=1
        outfile.write('Case #'+str(j)+': '+output+'\n')
        
       
    
    infile.close()
    outfile.close()