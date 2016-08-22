test = int (raw_input())
for t in range(test):
    s=raw_input()
    apple=s[0]
    s=s[1:]
    for i in s:
        if ord(i)>=ord(apple[0]):
            apple=i+apple
        else:
            apple+=i
            
    answer="Case #"+str(t+1)+":"
    print answer,apple
    
