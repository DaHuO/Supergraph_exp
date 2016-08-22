def solve(in_file, out_file):
    trials=int(in_file.readline())
    for trial in range(1, trials + 1):
        cakes = in_file.readline().strip()
        moves = 0
        prev = cakes[0]
        for c in cakes[1:]:
            if c!=prev:
                moves += 1
            prev = c
        if cakes[-1] == '-':
            moves += 1
        out_file.write("Case #{}: {}\n".format(trial, moves))
        
if __name__ == '__main__':
    path='Data/'
    #name='B-sample'
    #name='B-small-attempt0'
    name='B-large'
    raw=open(path+name+'.in', 'r')
    wrt=open(path+name+'.out','w')
    solve(raw, wrt)
    raw.close()
    wrt.close()