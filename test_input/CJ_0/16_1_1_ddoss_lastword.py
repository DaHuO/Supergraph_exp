import sys

def main():
    num_cases = int(sys.stdin.readline())
    cases = [sys.stdin.readline().strip() for i in range(num_cases)]
    for i in range(num_cases):
        print("Case #"+str(i+1)+": "+str(solve(cases[i])))

def solve(case):
    ans_str = case[0]
    for i in range(1, len(case)):
        if ord(case[i])>=ord(ans_str[0]):
            ans_str = case[i]+ans_str
        else:
            ans_str = ans_str+case[i]
    return ans_str
        

if __name__=='__main__':
    main()
