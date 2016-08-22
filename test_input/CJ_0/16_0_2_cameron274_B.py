def flip(S, n):
    #flips the top n pancakes
    for i in range(n):
        if S[i] == "+":
            S[i] = "-"
        elif S[i] == "-": S[i] = "+"
    flipped = S[:n]
    flipped.reverse()
    return flipped + S[n:]

def run_test():
    S = list(raw_input())
    # print(S)
    flips = 0
    for b_index in range(len(S)-1, -1, -1):
        if (S[b_index] == "-"):
            if (S[0] == "+"):
                plus_index = b_index-1
                while (S[plus_index] == "-"):
                    plus_index -= 1
                S = flip(S, plus_index+1)
                # print(S, "plus", (plus_index+1))
                flips += 1
            S = flip(S, b_index+1)
            # print(S, "back", (b_index+1))
            flips += 1
    return flips

t = int(raw_input())
for i in range(1, t+1):
    print("Case #%d: %d" % (i, run_test()))