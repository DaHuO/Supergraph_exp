T = int(raw_input())

for case in range(T):
    S = raw_input().strip()
    final = ""
    for char in S:
        if final == "":
            final = char
        else:
            first_one = max(final[0], char)
            final = char+final if first_one == char else final+char
    print "Case #{}: {}".format(case+1, final)
