def flip(case):

    stack = str(input())
    present_sign = stack[0]
    i=1
    flip_count = 0
    while i < len(stack):
        if stack[i] != present_sign:
            flip_count = flip_count+1
            present_sign = stack[i]
        i = i+1
    if present_sign == '-':
        flip_count = flip_count+1
    print("Case #", case,": ", flip_count, sep='')



T = int(input())
for i in range(1,T+1):
    flip(i)
