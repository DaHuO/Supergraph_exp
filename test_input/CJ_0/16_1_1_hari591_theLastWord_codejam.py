t = input()

i = 0
while t:
    i += 1
    t-=1
    s = raw_input().strip()
    final = ""

    for each in s:
        if final == "":
            final = each
            continue

        if ord(each) >= ord(final[0]):
            final = each + final
        else:
            final = final + each
    print "Case #" + str(i) + ": " + final