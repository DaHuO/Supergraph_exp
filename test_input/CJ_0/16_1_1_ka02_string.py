t = int(raw_input())
test = t
while t > 0:
    s = raw_input()
    m = max(s)
    count = 0
    new = f = ''
    
    for i in range(0, len(s)):                       
        if s[i] >= f:
            new = s[i] + new
            f = new[0]            
        else:
            new = new + s[i]
            f = new[0]           
                
    ans = (count * m) + new
    print "Case #" + str(test - t + 1) + ":" + " " + str(ans)
    t -= 1