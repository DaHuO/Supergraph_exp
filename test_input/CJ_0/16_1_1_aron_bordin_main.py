for t in range(int(input())):
    s = list(input())
    word = [s.pop(0)]
    for l in s:
        if l >= word[0]:
            word.insert(0, l)
        else:
            word.append(l)

    print("Case #%d: %s" % (t + 1, ''.join(word)))
