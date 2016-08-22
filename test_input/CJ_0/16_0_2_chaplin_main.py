def problem_2016B():
    t=int(raw_input())
    for case in range(1,t+1):
        s=raw_input()
        count = 1
        if s.endswith('+'):
            count = 0
        L=len(s)
        for i in range(1,L):
            if not s[i] == s[i-1]:
                count = count + 1
        print 'Case #' + str(case) + ': ', count 

def main():
    problem_2016B()
    
if __name__ == '__main__':
    main()
