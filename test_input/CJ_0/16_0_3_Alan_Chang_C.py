# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

N = 32
J = 500

print("Case #1: ")

count = 0
M = N//2

odd3 = M-1
even1 = 0

for odd1 in range(0, M-1):
    for odd2 in range (odd1+1, M-1):
        for even2 in range(1, M):
            for even3 in range(even2+1, M):
                num = (1 << 2*odd1+1) + (1 << 2*odd2+1) + (1 << 2*odd3+1) + (1 << 2*even1) + (1 << 2*even2) + (1 << 2*even3)
                print("{0:b}".format(num) + " 3 4 5 6 7 8 9 10 11")
                count += 1
                if count == J:
                    quit()

print("didn't find enough! fix your code!")