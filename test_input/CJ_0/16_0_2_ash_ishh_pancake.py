# Pancackes GCJ
# Ash-Ishh..

T = int(input())

for case in range (1,T+1):
    answer = 0
    a = input()
    stack = list(a)
    
    def all_minus(answer):
        if not '+' in stack:
            answer += 1
            final_ans(answer)
        else:
            all_plus(answer)
    
    def all_plus(answer):        
        if not '-' in stack:
            final_ans(answer)
        else:
            if stack[0] == '-':
                minus_first(answer)
            else:
                plus_first(answer)
                
    def minus_first(answer):
        for each in stack:
            if each == '-':
                stack.insert(stack.index(each)+1,'+')
                stack.pop(stack.index('-'))
            else:
                break
        answer += 1
        all_minus(answer)
        
        
    def plus_first(answer):
        for each in stack:
            if each == '+':
                stack.insert(stack.index(each)+1,'-')
                stack.pop(stack.index('+'))
            else:
                break
        answer += 1
        all_minus(answer)
             
     
     
    def final_ans(answer):           
        print("Case #{0}: {1}".format(case,answer))
        
    all_minus(answer)
    