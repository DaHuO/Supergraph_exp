abcs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
abc_dict = {y:x for x, y in enumerate(abcs, 1)}

def winning(S):
    winner = []
    for c in S:
        if winner == []:
            winner.append(c)
        else:
            if abc_dict[c] >= abc_dict[winner[0]]:
                winner.insert(0, c)
            else:
                winner.append(c)
    return ''.join(winner)

def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        s = raw_input()
        print 'Case #%s: %s' % (i, winning(s))

main()
