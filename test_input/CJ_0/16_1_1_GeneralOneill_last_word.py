def last_word(line_in):
    out = ""
    for char in line_in:
        if len(out) == 0:
            out += char
            continue
        if out[0] > char:
            out += char
        else:
            out = char + out
    return out

cases = int(raw_input())
for case in range(cases):
    line_in = raw_input()
    out = last_word(line_in)
    print("Case #" + str(case+1) + ": " + out)
