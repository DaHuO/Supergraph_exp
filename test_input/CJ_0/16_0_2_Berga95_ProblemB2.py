def flip(s,n):

    s2 = s[:n]
    s2.reverse()
    s=s2[:]+s[n:]
    
    for x in range(0,n):
        if s[x] == '+':
            s[x]='-'
        else:
            s[x]='+'
    return s


f = open("input.in", "r")
fout = open("output.out", "w")
tot = f.readlines()

T = int(tot[0])



for i in range(1,T+1):
    line = tot[i].strip().split(" ")
    pan = list(line[0])[:]
    #print pan
    n=0
    for x in range(1,len(pan)):
        if( pan[x-1]!=pan[x]):
            pan = flip(pan,x) # inverto tutti tranne x. il ciclo mantiene invariante
            # pan[0..x-1] uguali e diversi da pan[x]
            # con questo flip ho ancora l'invariante pan[0..x] tutti uguali
            n=n+1
    if pan[-1] == '-':
        pan= flip(pan,len(pan))
        n=n+1



    #print pan
    #print "Case #{0}: {1}\n".format(i,n)
    fout.write("Case #{0}: {1}\n".format(i,n))
    
fout.close()
f.close()

