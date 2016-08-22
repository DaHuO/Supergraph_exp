# -*- coding: utf-8 -*-

#file_in = "A-test.in"
#file_out = "A-test.out"
#file_in = "A-small-attempt0.in"
#file_out = "A-small-attempt0.out"
file_in = "A-large.in"
file_out = "A-large.out"

with open(file_in, "r") as fin, open(file_out, "w") as fout:
    T = int(fin.readline().strip())
    for case in range(1, T + 1):
        S = fin.readline().strip()
        L = []
        for c in S:
            if len(L) == 0 or c >= L[0]:
                L.insert(0, c)
            else:
                L.append(c)
        last = "".join(L)
        print("Case #{0}: {1}".format(case, last))
        fout.write("Case #{0}: {1}\n".format(case, last))
print("done")
