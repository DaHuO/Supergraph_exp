'''
Created on 13.04.2013

@author: Alex
'''
def analyse(l):
    count = 0
    while '-' in l:
        if l[0] == '+':
            i = 0
            while l[i] == '+':
                l[i] = '-'
                i += 1
            count += 1
        last_minus = "".join(l).rfind('-') + 1
        to_flip = l[:last_minus]            
        for i in range(0,last_minus):
            if to_flip[i] == '-':
                to_flip[i] = '+'
            else:
                to_flip[i] = '-'
            l[last_minus-i-1] = to_flip[i]
        count += 1 
    return str(count)

if __name__ == '__main__':
    f = open('in/B-large.in', mode='r')
    g = open('out/B-large.out', mode='w')
    t = int(f.readline())
    for i in range(0,t):
        l = list(f.readline())
        g.write('Case #' + str(i+1) + ': ' + analyse(l) + '\n') 