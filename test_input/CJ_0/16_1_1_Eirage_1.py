file = open('A-large.in', 'r')
out = open('result.out','w')
T = int(file.readline())
#n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

for k in range (T):
    S = file.readline()
    ans = S[0]
    S = S[1:-1]
    for s in S: 
        if s >= ans[0]:
            ans = s + ans
        else:
            ans = ans + s

    
    out.write('Case #' + str(k+1) + ': ' + ans + '\n')
out.close()

