for t in range(int(input())):
    pancakeStack = input()
    flips = 0
    if (len(pancakeStack) != 0):
        # Read from right to left
        bottomPancake = ""
        pancakeBellow = ""
        for pancake in reversed(pancakeStack):
            if (pancakeBellow != ""):
                if(pancake != pancakeBellow):
                    flips += 1
            else:
                bottomPancake = pancake
            pancakeBellow = pancake
        if bottomPancake == "-":
            flips += 1
    print("Case #" + str(t+1) + ": " + str(flips))
        
