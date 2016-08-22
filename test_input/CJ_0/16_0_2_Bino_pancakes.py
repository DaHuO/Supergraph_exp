def pancake_flips(P):
    flips = 0
    last = ''
    for i in range(len(P)):
        # print("Pi: " + P[i])
        if i == 0:
            last = P[i]
        elif P[i] != last:
            flips = flips+1
            last = P[i]
    if last == '-':
        flips = flips+1
    return flips

if __name__ == "__main__":
    input = "B-large"
    f = open(input + ".in")
    output = open(input + ".out", "w")
    cases = int(f.readline())
    for i in range(cases):
        P = list(f.readline().strip())
        output.write("Case #" + str(i+1)+ ": " + str(pancake_flips(P))+"\n")
    f.close()
    output.close()