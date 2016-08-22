case=[]
with open('/Users/cindy_liao/Downloads/A-small-attempt1.in','r') as file1:
    case_num=file1.readline()
    case=file1.readlines()
for i in range(int(case_num)):
    case[i]=case[i].strip()

def last_word(s):
    words=[]

    for i in range(2**(len(s)-1)):
        word=[s[0]]
        #word.append(s[0])
        for j in range(len(s)-1):
            if (i>>j)%2==0:
                word.insert(0,s[j+1])
            else:
                word.append(s[j+1])
        words.append(word)
    w=''
    for i in sorted(words)[-1]:
        w+=i
    return(w)




for i in range(len(case)):
    with open('/Users/cindy_liao/Desktop/1.txt','a') as file2:
        file2.write('Case #'+str(i+1)+': '+str(last_word(case[i]))+'\n')
