t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    count = 0
    while True:
        rindex = s.rfind("-")
        if rindex == -1:
            print "Case #{}: {}".format(i, count)
            break
        elif rindex == 0:
            count += 1
            print "Case #{}: {}".format(i, count)
            break
        else:
            if s[0] == '+':
                pos_rindex = s[:rindex].rfind('+')
                left = ""
                j = pos_rindex
                while j >= 0:
                    if s[j] == '+':
                        left += '-'
                    else:
                        left += '+'
                    j -= 1
                right = s[pos_rindex+1 : ]
                s = left + right

                count += 1
            else:
                left = ""
                j = rindex
                while j >= 0:
                    if s[j] == '+':
                        left += '-'
                    else:
                        left += '+'
                    j -= 1
                right = s[rindex + 1 : ]
                s = left + right

                count += 1




    

