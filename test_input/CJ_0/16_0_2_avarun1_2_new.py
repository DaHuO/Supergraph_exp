def main():
    f_inp = open('B-large.in')
    f_out = open('B.out', 'w')
    inp = f_inp.read().split('\n')
    inp = inp[:-1]
    n = int(inp[0])
    for question_index in xrange(1, n + 1):
        pancake_stack = inp[question_index]
        temp = pancake_stack[0]
        count = 0
        for sign in pancake_stack:
            if not sign == temp:
                count += 1
                temp = sign
        if pancake_stack[len(pancake_stack) - 1] == '+':
            f_out.write('Case #'+str(question_index)+': '+str(count)+'\n')
        else:
            f_out.write('Case #'+str(question_index)+': '+str(count+1)+'\n')

if __name__ == '__main__':
    main()
