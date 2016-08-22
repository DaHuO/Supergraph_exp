
def last_word(ordet):
    svar = ordet[0]
    ordet = ordet[1:-1]
    bokstavVerdi = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,\
    'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,\
    'W':23,'X':24,'Y':25,'Z':26}
    for char in ordet:
        if bokstavVerdi[char] >= bokstavVerdi[svar[0]]:
            svar = char+svar
        else:
            svar = svar+char
    return svar





def main():
    fil = open('A-large.in','r')
    output = open('output.txt','w')
    cases = fil.readline()
    for i in range(int(cases)):
        ordet = fil.readline()
        svaret = last_word(ordet)
        print("Case #"+str(i+1)+": "+svaret)
        output.write("Case #"+str(i+1)+": "+svaret+"\n")
    output.close()
    fil.close()

main()
