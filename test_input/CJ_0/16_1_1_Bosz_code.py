
T = int(raw_input())
for case in range(1,T+1):
    S = raw_input()
    last = ''
    for c in S:
        if(len(last)==0): last=c
        else:
            firstword = last[0]
            if(c>=firstword):
                last = c+last
            else:
                last = last+c


    print 'Case #{}: {}'.format(case,last)
