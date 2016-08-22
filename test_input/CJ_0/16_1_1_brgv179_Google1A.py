test_cases = int(raw_input())
def CheckisLastword(word,test):
    mystring=word[0];
    for c in word[1:]:
        if(c<mystring[0]):
           mystring=mystring+c
        if(c>=mystring[0]):
           mystring=c+mystring
    print "Case #"+str(test+1)+": "+mystring
for test in range(test_cases):
    word = (raw_input())
    CheckisLastword(word,test)
