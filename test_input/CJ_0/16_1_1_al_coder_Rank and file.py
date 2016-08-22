from array import array
data = open('A-large (2).in','r')
d = open('A-large (2).out','w')

cases = data.readline()
case_count = 1
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while (case_count <= int(cases)):
    word = data.readline()

    spword = word.strip()
    val = len(spword)
    count = 0
    ans = spword[0]
    
    while (count < val):
        done = 0
        count1 = 0
        
        while done == 0:
            #print(alph[count1],spword[count])
            if alph[count1] == spword[count]:
                num = count1
                done = 1
            count1 += 1
            
        if count == 0:
            left = count1
            right = count1
        else:
            if count1 >= left:
                ans = spword[count] + ans
                left = count1
            else:
                ans = ans + spword[count]
                right = count1
        #print(ans,case_count,count1)
        count += 1
        
    james = 'Case #' + str(case_count) +': ' + ans
    print(james,file = d)
    case_count += 1
d.close()
