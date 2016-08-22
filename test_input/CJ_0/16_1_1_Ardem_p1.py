fin = open('A.in', 'r')
fout = open('file.out', 'w')
n = fin.readline()
for l in range(int(n)):
    letters = list(fin.readline().strip())
    out = letters[0]
    #print letters
    for c in letters[1:]:
        if ord(c) < ord(out[0]):
            #print c,out[0]
            out += c
        else:
            #print c,out[0], '*'
            out = c + out
    fout.write('Case #%d: %s\n'%(l+1,out))

fin.close()
fout.close()
