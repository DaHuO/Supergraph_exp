I = open('A-large.in', 'r')
O = open('output.txt', 'w')

cases = 0

N = I.readline()

for line in I:
    cases += 1
    count = 1
    S = line.rstrip('\n')
    word = ""

    for char in S:
        if len(word) == 0:
            word = char
        else:
            if ord(char) >= ord(word[0]):
                word = char+word
            else: word = word+char

    O.write("Case #"+str(cases)+": "+word+"\n")


I.close()
O.close()
    
