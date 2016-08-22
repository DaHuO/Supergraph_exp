##
## Google Code Jam 2016
## Round 1A, Apr 16
##
## Problem Title: The Last Word
## Author: James Hall
## Email: james.hall@infinityworks.com
##

alp = { }
def calculate(t):

    result = t[0]
    
    for i in t[1:]:
        if i < result[0]:
            result = result + i
        else:
            result = i + result

    return result

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t + 1):
        x = raw_input()
        result = calculate(x)
        print("Case #{}: {}".format(i, result))

