t = int(input()) 
for i in range(1, t + 1):
    S = str(input()) 
    A = S[0]
    first_letter = S[0]
    S = S[1:]
    for ltr in S :
        if ord(first_letter) > ord(ltr):
            A = A + ltr
            first_letter = A[0]
        else :
            A = ltr + A
            first_letter = A[0]
    print("Case #{}: {} ".format(i, A))
        