for _ in range(input()):
    w = list(raw_input())
    a = ''
    a +=w[0]
    for i in w[1:]:
        if a[0]<=i:
            a = i + a
        else:
            a = a+i
    print "Case #%d:"%(_+1),a
