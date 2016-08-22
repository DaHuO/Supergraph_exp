# python2

fin = open('B.in' , 'r')
fout = open('B.out' , 'w')

T = fin.readline()
T = int(T)

for t in range(1 , T+1):
    s = fin.readline()
    count = 0
    while True:
        if '-' not in s:
            break
        else:
            i = 0
            w = s[i]
            while i < len(s) and s[i] == w:
                if s[i] == '-':
                    s = s[0:i] + '+' + s[i+1 : ]
                else:
                    s = s[0:i] + '-' + s[i+1 : ]
                i += 1
            count += 1
    fout.writelines('Case #'+str(t)+': '+str(count)+'\n')

fin.close()
fout.close()
