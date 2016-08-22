# problem 11024
"""
n = int(raw_input())
for i in range(n):
    print sum(map(int, raw_input().split()))
"""
# problem 1002
"""
a = []
for i in range(input()):
    a.append(map(int,raw_input().split()))

    d = pow(a[i][0]-a[i][3],2) + pow(a[i][1]-a[i][4],2)
    x = pow(a[i][2]+a[i][5],2)
    y = pow(a[i][2]-a[i][5],2)

    if d == 0 and a[i][2] == a[i][5]:
        print -1
    elif x == d or y == d:
     print 1
    elif x < d or y > d:
        print 0
    else:
        print 2
"""
# problem 11718 not done
"""
while(1):
    a = raw_input()
    if len(a) == 0:
        break
    print a
"""
# problem 11066


"""
# problem 11531

cnt = 0

while(1):
    a = raw_input().split()
    if a[0]=='-1':
        break
    if a[2]=='right':
        cnt+=1
"""
"""
# CodeJam #1
digit = [0,0,0,0,0,0,0,0,0,0]

cnt = 1
f = open('A-large.txt','r')
fw = open('A-large.out','w')
T = f.readline()

for i in range(int(T)):
    N = f.readline()
    if not N:
        break
    print N

    while True:
        if int(N) == 0:
            fw.write('Case #'+str(i+1)+': '+'INSOMNIA\n')
            break
        n = int(N)*cnt
        x = 10**(len(str(n))-1)
        #print x
        while x>=1:
            k = n/x
            #print n,k
            n = n-(k*x)
            x = x/10
            if digit[k] == 0:
                digit[k] += 1
        if sum(digit) == 10:
            digit = [0,0,0,0,0,0,0,0,0,0]
            fw.write('Case #'+str(i+1)+': '+str(int(N)*cnt)+'\n')
            cnt = 1
            break
        cnt+=1

f.close()
fw.close()
"""

# CodeJam #2
"""
def pop_stack(stack, bot):
    while stack[bot] == '+':
        stack.pop()
        if bot-1 >= 0:
            bot -= 1
        else:
            break
    return stack

def main():
    f = open('B-large.txt','r')
    fw = open('B-large.out','w')
    T = f.readline()


    for n in range(int(T)):
    #for n in range(1):
        tmp = f.readline()
        stack = []
        for i in range(len(tmp)):
            if tmp[i] == '\n':
                break
            stack.append(tmp[i])

        print stack

        cnt = 0
        plus_cnt = 0
        while True:
            pos = len(stack)
            bot = pos-1

            if not stack:
                print 'stack is empty'
                break

            if pos == 1:
                if stack[0] == '+':
                    break
                else:
                    cnt += 1
                    break

            elif stack[0] == '-' and stack[pos-1] == '-':
                for i in range(pos):
                    if stack[i] == '+':
                        stack[i] = '-'
                    else:
                        stack[i] = '+'
                stack.reverse()
                pop_stack(stack,bot)
                cnt += 1

            elif stack[0] == '+' and stack[pos-1] == '+':
                for i in range(pos):
                    if stack[i] == '+':
                        plus_cnt += 1
                if plus_cnt == pos:
                    break

                i=0
                while stack[i] == '+':
                    if i < bot:
                        i += 1
                    else:
                        break
                for j in range(i):
                    if stack[j] == '+':
                        stack[j] = '-'
                pop_stack(stack,bot)
                cnt += 1

            elif stack[0] == '-' and stack[pos-1] == '+':
                i=0
                while stack[i] == '-':
                    i += 1
                for j in range(i):
                    if stack[j] == '-':
                        stack[j] = '+'
                pop_stack(stack,bot)
                cnt += 1
            elif stack[0] == '+' and stack[pos-1] == '-':
                i=0
                while stack[i] == '+':
                    i += 1
                for j in range(i):
                    if stack[j] == '+':
                        stack[j] = '-'
                stack[0:j].reverse()
                pop_stack(stack,bot)
                cnt += 1

        fw.write('Case #'+str(n+1)+': '+str(cnt)+'\n')
        #print 'Case #'+str(n+1)+': '+str(cnt)+'\n'

    f.close()
    fw.close()


main()
"""

# CodeJam #3

"""
f = open('C-small-attempt0.txt','r')
fw = open('C-small-attempt1.out','w')

n_case = [2,3,4,5,6,7,8,9,10]
jc_bi = []
jc_div = []
bi = 0
cnt = 0
T = f.readline()
line = f.readline()
N = int(line.split(' ')[0])
J = int(line.split(' ')[1])
S = bin(2**(N-1)+1)[2:N+2]


while True:
    S = bin(int(S,2)+2*cnt)[2:N+2]
    n_result = []
    jc = []
    jc_result = []
    div = 2
    isPrime = 0

    if cnt == J:
        print 'Done!'
        break

    for i in range(len(S)):
        jc.append(S[i])

    for i in n_case:
        bi = 0
        for j in range(len(jc)):
            bi = bi + int(jc[len(jc)-j-1])*i**j
        n_result.append(bi)

    for i in range(len(n_result)):

        bi = n_result[i]

        while True:
            if div > 100000:
                break;
            if bi%div == 0:
                jc_result.append(str(div))
                isPrime += 1
                break
            div += 1

    if isPrime == 9:
        jc_div.append(" ".join(jc_result))
        jc_bi.append("".join(S))
        cnt += 1

fw.write('Case #1:'+'\n')
for i in range(len(jc_bi)):
    fw.write(jc_bi[i]+' '+jc_div[i]+'\n')

f.close()
fw.close()

"""

# Codejam round 1-A #1





f = open('A-large.txt','r')
fw = open('A-large.out','w')
t = int(f.readline())
for k in range(t):
    s=[]
    r=[]
    S = f.readline().split()

    for j in range(len(S[0])):
        s.append(S[0][j])



    for i in range(len(s)):
        if i == 0:
            r.append(s[i])

        else:
            if r[0] > s[i]:
                r.insert(len(r),s[i])
            else:
                r.insert(0,s[i])

    fw.write('Case #'+str(k+1)+': '+"".join(r)+'\n')