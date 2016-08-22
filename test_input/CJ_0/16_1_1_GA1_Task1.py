'''
@author: Kamil
'''

def task1(S):
    word = S[0]
    for i in range(1, len(S)):
        s = S[i]
        if ord(s) >= ord(word[0]):
            word = s + word
        else:
            word = word + s
    return word       
       

            
 
f = open('output.txt','w')
  
with open('A-large.in') as file:
    lines = file.readlines()
    for i in range(1, len(lines)):
        line = lines[i].replace('\n', '').replace('\r', '')
        n = (line)
        print("Case #" + str(i) + ": " + str(task1(n)))
         

            
    