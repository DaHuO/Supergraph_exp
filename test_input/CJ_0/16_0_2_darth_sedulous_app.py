import sys

def main ():

    T = int (sys.stdin.readline ().strip ())

    for t in range (T):

        states = list (sys.stdin.readline ().strip ())
        answer = 0
        position = len (states) - 1

        for p in reversed (range (position + 1)):

            if states [p] == "-":

                if states [0] == "+":

                    states = flip (states, states.index ("-"))
                    answer += 1

                states = flip (states, p + 1)
                answer += 1

        print ("Case #{}: {}".format (t + 1, answer))

    return 0

def flip (states, number):

    states = list (reversed (states [0:number])) + states [number:]

    for n in range (number):

        states [n] = "+" if states [n] == "-" else "-"
    
    return states

if __name__ == "__main__":

    exit (main ())
