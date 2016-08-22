import sys, math

def main():
    data = sys.stdin.readlines()
    for i in range(1, len(data)):
        data = list(data[1].split(' '))
        print('Case #1:')
        solve(int(data[0]), int(data[1]))

        

def solve(n, j):
    first = int('1' + ((n-2) * '0') + '1', 2)
    last = int('1'*n,2)
    found = 0
    for i in range(first, last+1, 2):
        n = bin(i)[2:]
        x = is_jamcoin(n)
        if False not in x:
            found += 1
            lst = list(map(str, x))
            print(n + ' ' + ' '.join(lst))
            if found >= j:
                break
                
def is_jamcoin(n):
    lst = []
    for i in range(2, 11):
        lst.append(find_divisor(int(n,i)))
        if False is lst:
            return False
    return lst
        
            
    
    


def find_divisor(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return i
    return False

if __name__ == "__main__":
    main()
