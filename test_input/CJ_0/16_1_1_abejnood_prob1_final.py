import csv, sys, random, math

def solve(word):
    word_len = len(word.rstrip('\n'))
    new_word = str(word[0])
    for i in xrange(word_len - 1):        
        if word[i + 1] >= new_word[0]:
            new_word = str(word[i + 1]) + new_word
        else:
            new_word = new_word + str(word[i + 1])
    return new_word
        

target = open("prob1_output_small.txt", 'w')
with open('prob1_small.txt','r') as f:
    T = int(f.readline())    
    for i in xrange(T):
        word = str(f.readline())
        case_num = str(i+1)
        sol_str = 'Case #' + case_num +  ': ' + str( solve(word)  ) + '\n'
        target.write( str(sol_str) )
        
    






