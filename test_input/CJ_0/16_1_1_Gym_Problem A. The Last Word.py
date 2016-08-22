
def last_word(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')

    for i in range(T):
        S = fr.readline().strip()
        word = S[0]
        for j in S[1:]:
            if j >= word[0]:
                word = j + word
            else:
                word = word + j

#         print('Case #%d: %s\n'%(i+1,word))
        fw.write('Case #%d: %s\n'%(i+1,word))

    fr.close()
    fw.close()

last_word('A-large.in')
