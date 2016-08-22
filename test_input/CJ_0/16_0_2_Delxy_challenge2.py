def solve(pile):
    ret = 0
    blocs = []
    while len(pile) > 0:
        i = 0
        last = pile[0]
        while i<len(pile) and pile[i] == last:
            i+=1
        blocs.append(pile[:i])
        pile = pile[i:]

    while len(blocs) > 1:
        if(blocs[0][0] == '+'):
            blocs[1] = blocs[1] + '-'*len(blocs[0])
        else:
            blocs[1] = blocs[1] + '+'*len(blocs[0])
        ret +=1
        blocs.pop(0)
    return str(ret if blocs[0][0] == '+' else (ret + 1))


t = int(raw_input())

for i in range(1, t+1):
    n = str(raw_input())
    print "Case #" + str(i) +": "+ solve(n)
