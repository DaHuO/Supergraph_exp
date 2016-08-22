# -*- coding:Utf-8 -*-
from sys import argv
from random import randint


def is_prime(n,d) : 
    if n <= 2 :
        print n,
        return False
    elif n == 2 :
        return True
    elif not n & 1 :
        d['div'].append('2')
        return False
    else : 
        for x in range(3, int(n**0.5) + 1, 2):
            if n % x == 0:
                d['div'].append(str(x))
                return False
    return True
    
def is_not_prime_in_all_base(jam,d) :
    d['div'] = []
    not_a_prime = True
    i = 2
    while not_a_prime and i < 11 :
        #print int(jam,i),
        if is_prime(int(jam,i),d) :
            not_a_prime = False
        i+=1
    return not_a_prime

def get_a_jam(length,d) :
    jamcoin = ''
    if length == 2 :
        jamcoin = "11"
    else :
        existing_coin = True
        while existing_coin :
            jamcoin = "1"
            for i in range(length-2) :
                j = str(randint(0,1))
                jamcoin = jamcoin + j
            jamcoin = jamcoin + "1"
            if not d.has_key(jamcoin) :
                existing_coin = False
        d[jamcoin]=None
    return jamcoin


def main() :
    f_input=argv[1:][0]
    f_output= open("coinjam_small.txt",'w')
    read_input = open(f_input,'r')
    nb_of_case = read_input.readline()
    nb_of_case = int(nb_of_case)
    d_solved = {}
    d_old = {}
    for i in range(nb_of_case) :
        line = read_input.readline()
        (n,j) = line.split()
        n=int(n)
        j=int(j)
        f_output.write("Case #"+str(nb_of_case)+":\n")
        while j != 0 :
            a_jam = get_a_jam(n,d_solved)
            #print a_jam,
            if not d_old.has_key(a_jam) :
                is_ok = is_not_prime_in_all_base(a_jam,d_solved)
                if is_ok :
                    f_output.write(a_jam + ' ' + ' '.join(d_solved['div']) + "\n")
                    d_old[a_jam]=d_solved['div']
                    j -=1
            else :
                f_output.write(a_jam + ' ' + ' '.join(d_old[a_jam]) + "\n")
                j -= 1
    #print is_prime(11)
    f_output.close()

    
    
if __name__ == "__main__" :
    main()