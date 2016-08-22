# Input files
fin = open('word.in', 'r')
fout = open('word.out', 'w')

T = int(fin.readline())
for t in range(0, T):
    S = fin.readline()
    winWord = S[0]
    for c in S[1:]:
        if c >= winWord[0]:
            winWord = c + winWord
        else:
            winWord = winWord + c
    fout.write("Case #" + str(t+1) + ": " + winWord)

# Output files
fin.close()
fout.close()