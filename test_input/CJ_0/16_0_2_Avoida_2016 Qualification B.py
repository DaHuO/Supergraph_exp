def main():
    problem = open("B-small-attempt1.in", "r")
    output = open("B-out.txt", "w")

    test = int(problem.readline().strip())

    for i in range(test):
        pancake = problem.readline().strip()
        possible = [pancake]
        flip = 0
        obj = "+" * len(pancake)
        while obj not in possible:
            cur = list()
            for pan in possible:
                for j in range(len(pan)):
                    flipped = pancakeFlip(pan, j+1)
                    if flipped not in cur:
                        cur.append(flipped)
            possible = cur[:]
            flip += 1
        output.write("Case #" + str(i+1) + ": " + str(flip) + "\n")
    problem.close()
    output.close()

def pancakeFlip(pancake, end):
    result = str()
    for i in range(end):
        if pancake[end-i-1] == "-":
            result += "+"
        else:
            result += "-"
    result += pancake[end:]
    return result

main()
