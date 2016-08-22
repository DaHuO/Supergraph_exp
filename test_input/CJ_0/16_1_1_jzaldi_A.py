infile = open('input.in','r')
outfile = open('output.out','w')

T = int(infile.readline())

for t in range(T):

    S = infile.readline()

    q = []
    for c in S:
        if len(q) == 0:
            q.append(c)
        else:
            if c >= q[0]:
                q.insert(0,c)
            else:
                q.append(c)


    outfile.write('Case #' + str(t+1)+': ')
    for i in range(len(q)-1):
        outfile.write(q[i])
    outfile.write('\n')

infile.close()
outfile.close()