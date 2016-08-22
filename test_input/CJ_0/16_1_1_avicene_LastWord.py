
__author__ = 'adilmezghouti'
# al = ['BAC','ACB','BCA','CAB']
# al.sort(reverse=True)
# print al

with open("input.txt","r") as f:
    cases = f.readline()

    for i in range(0,int(cases),1):
        word = []
        word_2 = []

        for letter in f.readline():
            if letter == '\n':
                break
            if len(word) == 0:
                word.append(letter)
            else:
                # print word
                for w in word:
                    # print w
                    word_2.append(str(w)+ str(letter))
                    word_2.append(str(letter) + str(w))
                word = word_2
                word_2 = []

        word.sort(reverse=True)
        print "Case #" + str(i + 1) + ": " + word[0]

