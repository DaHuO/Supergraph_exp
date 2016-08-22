def inp():
    l = []
    fl =[]
    n = int(input())
    for i in range(n):
        l.append(input())
        s = l[i]
        fs = ''
        fs += s[0]
        for i in s[1:]:
            if(ord(i) >= ord(fs[0])):
                fs = i + fs
            else:
                fs = fs + i
        fl.append(fs)
    j = 1
    for i in fl:
        print("Case #",j,": ",i,sep='')
        j+=1

inp()

        
    
