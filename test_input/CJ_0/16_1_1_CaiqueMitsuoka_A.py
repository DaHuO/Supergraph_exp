casos = int(input())
for a in range(1,casos + 1):
    strr = str(input())
    strr = list(strr)
    nstrr = []
    primeira = '0'
    for letter in strr:
        if letter >= primeira:
            nstrr.append(letter)
            primeira = letter
        else:
            nstrr.insert(0,letter)
    nstrr.reverse()
    print("CASE #{}: {}".format(a,''.join(nstrr)))
