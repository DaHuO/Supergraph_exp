t=int(raw_input(''))

for i  in range(1,t+1):
    s = raw_input('')
    ans = s[0]
    for j in s[1:]:
        if j < ans[0]:
            ans = ans+j
        else:
            ans = j + ans
    print 'Case #%d:'%i, ans


        

