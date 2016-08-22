li = []
f = [li.append(line.rstrip()) for line in open('/Users/prajjwaldangal/Downloads/A-small-attempt0 (1).in')]
testcases = int(li[0])

def find_last_word(word):
    
    if word == "" or word == " ":
        last_word = word
    
    last_word = word[0]
    for i in range(1, len(word)):
        if word[i] >= last_word[i-1]:
            last_word += word[i]
        else:
            last_word = word[i] + last_word
    return last_word[::-1]

'''
Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE
'''

out = open('/Users/prajjwaldangal/Desktop/codejam_out.txt','w')      

for i in range(1, testcases+1):
    last_word = find_last_word(li[i])
    out.write("Case #"+str(i)+": "+str(last_word)+"\n")
out.close()