for l in range(int(input())):
    X = input()
    A = []
    i = 0 #index of word
    w = X[i]
    A.append(w)
    s = 0
    while(i != len(X)-1):
        for K in range (pow(2,i)):
            w = A[s]
            wordA = w + X[i+1]
            wordB = X[i+1] + w
            A.append(wordA)
            A.append(wordB)
            s += 1
        i += 1
    A.sort()
    print ("Case #{0}: {1}".format(l+1,A[len(A)-1]))