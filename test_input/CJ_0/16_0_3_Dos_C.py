"""
Created on 02/05/2015

@author: Dos

Problem C. Coin Jam
https://code.google.com/codejam/contest/6254486/dashboard#s=p2


***Sample***

Input
1
6 3

Output
Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11

"""
from random import randint
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, ]


def get_rand(dim):
    l = [str(randint(0, 1)) for i in range(dim-2)]
    return "1" + "".join(l)+"1"


def read_word(f):
    return next(f).strip()


def read_int(f, b=10):
    return int(read_word(f), b)


def read_words(f, d=' '):
    return read_word(f).split(d)


def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]


# INPUT_FILE_NAME = "C-sample.in"
# INPUT_FILE_NAME = "C-small-attempt0.in"
INPUT_FILE_NAME = "C-large.in"

# OUTPUT_FILE_NAME = "C-sample.out"
# OUTPUT_FILE_NAME = "C-small-attempt0.out"
OUTPUT_FILE_NAME = "C-large.out"

if __name__ == '__main__':

    # create I/O files
    input_file = open(INPUT_FILE_NAME, 'r')
    output_file = open(OUTPUT_FILE_NAME, "w")

    # read file size
    T = read_int(input_file)
    print("\nThere are %d cases to solve! :)\n" % T)

    # iterate on each case
    for case in xrange(1, T+1):
        # read input args
        line_1 = read_ints(input_file)
        N = line_1[0]  # 16
        J = line_1[1]  # 50

        print("Case #1:")
        output_file.write("Case #1:\n")

        good_nums = []
        while len(good_nums) < J:

            curr = get_rand(N)

            converted = [int(curr, base) for base in range(2, 11)]
            divisors = []

            for c in converted:
                div = 0
                for p in primes:
                    if (c % p) == 0:
                        div = p
                        break
                divisors.append(div)

            if (not 0 in divisors) and (not curr in good_nums):
                good_nums.append(curr)

                output_file.write(str(curr))
                print(str(curr))
                for b in divisors:
                    output_file.write(" " + str(b))
                    print(" " + str(b))

                output_file.write("\n")

    # close I/O files
    input_file.close()
    output_file.close()
