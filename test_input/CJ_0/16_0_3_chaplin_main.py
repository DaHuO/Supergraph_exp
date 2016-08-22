
def problem_2016C():
    t=int(raw_input())
    for case in range(1,t+1):
        N,J=[int(item) for item in (raw_input().split())]
        if N%2 == 0:
            m = (N-2)/2;
            mask=0
            found = 0
            print 'Case #'+str(case)+':'
            while found<J:
                a=mask
                bit=0
                solution = [1]+[0 for i in range(N-2)]+[1]
                while a>0:
                    if a%2 == 1:
                        solution[2*bit+1]=1
                        solution[2*bit+2]=1
                    a = a/2
                    bit = bit + 1
                print ''.join([str(item) for item in solution]), '3 4 5 6 7 8 9 10 11'
                found = found + 1
                mask = mask + 1
                    
def Ctest():
    f=open(r'c:\users\jsard\workspace\jam\files\c-small.out')
    lines = f.readlines()
    for line in lines[1:]:
        a=line.split()[0]
        print 'testing', a,'...',
        flag=True
        for b in range(2,10):
            n = 0
            p = 1
            for c in reversed(a):
                if c == '1':
                    n = n + p
                p = p * b
            if not n%(b+1)==0:
                flag = False
        print flag  
                
                            
        
        
        
def main():
    problem_2016C()
    #Ctest()

    
if __name__ == '__main__':
    main()
