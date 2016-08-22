
def solve(infile, outfile):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cases = int(infile.readline())

    for i in range(cases):
        word = infile.readline().strip("\n")
        result = word[0]
        for char in word[1:]:
            if alpha.index(char) >= alpha.index(result[0]):
                result = char + result
            else:
                result = result + char
            #print(result)
        outfile.write("Case #{}: {}\n".format(i + 1, result))    


if __name__ == '__main__':
    path = 'Data/'
    #name='A-sample'
    #name='A-small-attempt0'
    name='A-large'
    
    infile = open(path+name+'.in', 'r')
    outfile = open(path+name+'.out','w')
    
    solve(infile, outfile)
    infile.close()
    outfile.close()