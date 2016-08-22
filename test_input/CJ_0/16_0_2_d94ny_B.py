t = int(raw_input())
for i in range(t):

    s = raw_input()
    print "Case #{0}:".format(i+1),
    zones = 1
    last_zone = s[0]
    for x in s:
        if x == last_zone:
            continue
        last_zone = x
        zones += 1

    print zones - 1 if last_zone == '+' else zones
