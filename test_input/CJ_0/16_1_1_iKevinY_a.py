n = int(raw_input().strip())
for case in range(n):
    letters = raw_input().strip()
    out = None
    for letter in letters:
        if out is None:
            out = letter
        else:
            if ord(letter) < ord(out[0]):
                out = out + letter
            else:
                out = letter + out

    print "Case #{}: {}".format(case + 1, out)

