
import sys
import random 


def main():

    T = int(sys.stdin.readline().strip())

    for i in range(0,T):

        [J,N]= map(int, sys.stdin.readline().strip().split())
        jam_string_map = dict()

        print( "Case #%d:" % (i+1))
        while N>0:
            N-=1
            [jam_string, div_list] = get_string(J, jam_string_map)
            jam_string_map[str(jam_string)]=1
            print ''.join(map(lambda x: '1' if x==1 else '0', jam_string)), ' '.join(str(x) for x in div_list)



def get_string(J, jam_string_map):

    L = [0]*J
    L[0]=1
    L[J-1]=1

    while True:
        for i in range(0,J-2):
            L[i+1] = random.randint(0,1)
    
        div_list = []
        if check_string(L, div_list) and not jam_string_map.has_key(str(L)):
            return [L,div_list]




def check_string(L, div_list):
    
    for i in range(2,11):
        num = convert_to_base(L,i)
        tmp=[]
        if check_if_prime(num,div_list):
            return False
    return True



def convert_to_base(L,b):

    num = 0 
    l = len(L)
    for i in range(0,l):        
        num += (b**i)*L[l-1-i]
    return num


def check_if_prime(num, div_list):

    for i in range(2,2**10):
        if (i> num/2):
            break
        if num%i == 0:
            div_list += [i]
            return False
    return True




#calling main function
main()

