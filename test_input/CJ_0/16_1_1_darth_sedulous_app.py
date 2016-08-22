import sys
import re

def main ():

    T = int (sys.stdin.readline ().strip ())

    for t in range (T):

        S = sys.stdin.readline ().strip ()
        
        answer = S [0]
        S = S [1:]

        for s in S:

            if s >= answer [0]:

                answer = s + answer

            else:

                answer = answer + s

        print ("Case #{}: {}".format (t + 1, answer))

    return 0

if __name__ == "__main__":

    exit (main ())
