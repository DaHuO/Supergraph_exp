tests=int(input())
for test in range(1,tests+1):
    st=input()
    l=len(st)
    last_word=st[0]
    for i in range (1,l):
        if last_word[0]<=st[i]:
            last_word=st[i]+last_word
        else:
            last_word+=st[i]
    print("Case #{}: {}".format(test,last_word))
