import os, sys

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223]
def get_divisor(n):
    if n in primes:
        return 0
    if n == 2 or n == 3:
        return 0
    if n == 4:
        return 2
    r = int(n**0.5)
    for p in primes:
        if p > r:
            break
        if n%p==0:
            return p
    primes.append(n)
    return 0

def to_base_10(num_as_list, from_base):
    result = 0
    e = 0
    for c in num_as_list[::-1]:
        result += c * (from_base**e)
        e += 1
    return result

if __name__=='__main__':
    #path = './B-small-attempt0.in'
    #path = './B-large.in'
    n = 32
    j = 500
    out = open('./out.txt','w',  newline='')
    out.write("Case #1:\n")
    for i in range(2**(n-2)):
        divisors=[]
        middle = '0'*(n-2) + bin(i)[2:]
        case = [1] + [int(x) for x in middle[-n+2:]] + [1]
        #print('**************')
        #print(case)
        for base in [2,3,4,5,6,7,8,9,10]:
            test = to_base_10(case, base)
            #print(test)
            d = get_divisor(test)
            #print(d)
            if d == 0:
                divisors = []
                break
            else:
                divisors.append(d)
        if divisors:
            print(j)
            print(case)
            print(divisors)
            out.write(''.join(map(str,case)))
            out.write(' ')
            out.write(' '.join(map(str,divisors)))
            out.write('\n')
            j -= 1
        if j == 0:
            break
    out.close()
    print('done')