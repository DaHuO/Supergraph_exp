# -*- coding: utf-8 -*-
import string

with open("A-large.in", "r") as fin, open("outA.out", "w") as fout:
    alpha = string.ascii_uppercase
    n = int(fin.readline().strip())
    for i in range(n):
        current = fin.readline().strip()
        word = ""
        for char in current:
            if word == "":
                word = char
            elif alpha.index(char) >= alpha.index(word[0]):
                word = char + word
            else:
                word = word + char

        fout.write("Case #{}: {}\n".format(i + 1, word))
