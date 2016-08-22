def solve(infile, outfile):
    cases = int(infile.readline().strip("\n"))
    for i in range(cases):
        cakes = infile.readline().strip("\n")
        count = cakes.count("-+") + cakes.count("+-")
        if cakes[-1] == "-":
            count +=1
        outfile.write("Case #{}: {}\n".format(i+1, count))


## haha! not needed!
#def flip(end, string):
    #to_flip = string[:end]
    #flipped = ""
    #for char in to_flip:
        #if char == "-":
            #flipped = "+" + flipped
        #else:
            #flipped = "-" + flipped
    #return flipped + string[end:]

if __name__ == '__main__':
    
    path = 'Data/'
    #name='B_test'
    #name='B-small-attempt0'
    name='B-large'
    
    infile = open(path+name+'.in', 'r')
    outfile = open(path+name+'.out','w')
    
    solve(infile, outfile)
    infile.close()
    outfile.close()