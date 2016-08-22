def main():
    with open("A-large.in", "r") as fin:
        with open("lastword.out", "w") as fout:
            fin.readline()
            line = fin.readline()
            i = 1
            while line != "":
                last = lastword(line)
                fout.write("Case #{0}: {1}".format(i, last))
                i += 1
                line = fin.readline()

def lastword(s):
    word = s[0]
    for char in s[1:]:
        if char + word < word:
            word = word + char
        else:
            word = char + word
    return word

if __name__=="__main__":
    main()
