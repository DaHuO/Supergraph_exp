
shortS = lambda S: S[:S.rfind('-') + 1]

if __name__=="__main__":
    T = input()
    
    for t in xrange(1, T+1):
        S = shortS(raw_input())
        c = 0
        while(S != ''):
            i = -1
            if S[0] == '-':
                i = len(S)
            else:
                for s in S:
                    if s != '+':
                        break
                    i += 1

            flip = ''.join(['-' if s == '+' else '+' for s in S[i::-1]]) + S[i+1:]
            S = shortS(flip)
            c += 1

        print("Case #%d: %d" % (t, c))

