with open('output.txt', 'w') as g:
    pass


with open('A-large.in') as f:
    lineBuf = f.readline()
    T = int(lineBuf)

    for cnt in range(T):
        s = f.readline()
        s.strip('\n')        

        result = ""
        result = result + s[0]
        
        for i in s[1:]:
            if i >= result[0]:
                result = i + result
            else:
                result = result + i


        with open('output.txt', 'a') as g:
            g.write('Case #'+str(cnt+1)+': '+result)

