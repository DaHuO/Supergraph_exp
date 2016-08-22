import sys

fd = open(sys.argv[1], 'r')

ncases = int(fd.readline()[:-1])

for case in range(1, ncases+1):
    word = fd.readline()[:-1]
    win = ''
    for char in word:
        if char >= win[:1]:
            win = char + win
        else:
            win = win + char

    print("Case #" + str(case) + ":", win)

