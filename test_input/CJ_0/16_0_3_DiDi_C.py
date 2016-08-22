T = int(input())

for K in range(T):
    N, J = input().split()
    N = int(N)
    J = int(J)
    print("Case #" + str(K+1)+ ": ")
    for a in range(J):
        s = bin(a)[2:]
        s = s.zfill(N//2-1)
        t = [x*2 for x in s]
        u = "1"+"".join(t)+"1"
        print(u, end = "")

        for b in range (2, 11):
            print("",b+1, end = "")
        print()