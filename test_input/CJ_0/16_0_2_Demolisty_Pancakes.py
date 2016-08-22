for O in range (int(input())):
    P = input()
    N = set(P)
    i = 0;
    if (len(P) == 1):
        if(P == '-'):
            i = 1
    else:
        while ("".join(N) != '+'):
            x = 1
            while(P[x] == P[x-1]):
                x += 1;
                if (x == len(P)):
                    break;
            S = list(P[:x])
            K = list(P[x:])
            for l in range(x):
                if S[l] == "+":
                    S[l] = "-"
                elif S[l] == "-":
                    S[l] = "+"
            Z = "".join(S)
            t = Z[::-1]
            P = t + "".join(K)
            N = set(P)
            i += 1
    print("Case #{0}: {1}".format(O+1,i))


