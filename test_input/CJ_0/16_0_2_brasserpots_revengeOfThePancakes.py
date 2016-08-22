# START SETUP #
modeWanted = input("b/s\n")
if modeWanted.upper() == "B":
    mode = "Big"
else:
    mode = "Small"
# GET FILES #
inputFile = open("inputs\\revengeOfThePancakes" + mode + ".in").readlines()
outputFile = open("outputs\\revengeOfThePancakes" + mode + "Out.txt", "w")
# MAIN #
caseNumber = 0
for case in inputFile[1:]:
    caseNumber += 1
    # TEST FOR END POSITIVE #
    if case.rstrip()[-1] == "+":
        count = -1
    else:
        count = 0
    prevChar = ""
    for char in case.rstrip():
        if char != prevChar:
            count += 1
        prevChar = char
    outputFile.write("Case #" + str(caseNumber) + ": " + str(count) + "\n")