#!/usr/bin/python3

T = int(input())

words = list()
for i in range(T):
    words.append(input())

for i_T, word in enumerate(words):
    # print(i_T, word)
    tmp = ''
    for letter in word:
        # print(ord(letter))
        if len(tmp) == 0:
            tmp = letter
        elif ord(tmp[0]) <= ord(letter):
            tmp = letter + tmp
        else:
            tmp = tmp + letter
    # print(tmp)


    print("Case #{}: {}".format(i_T+1, tmp))
