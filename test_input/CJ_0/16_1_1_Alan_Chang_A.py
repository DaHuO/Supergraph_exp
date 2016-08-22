# python 3.4 !!

#from functools import lru_cache
#@lru_cache(maxsize = None)

num_trials = int(input())

def compute():
    S = input()
    l = len(S)

    win = ""
    for i in S:
        option_front = i + win
        option_back = win + i
        win = max(option_front, option_back)

    return win

for i in range (0, num_trials):
    print("Case #" + str(i+1) + ": " + compute())
