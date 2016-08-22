#open the file
file = open('B-large.in','r')
lines = file.readlines()

# number of test cases
T = int(lines[0])

for testCase in range(1, T+1):
    numFlips = 0
    pancakeStack = lines[testCase].strip()
    while('-' in pancakeStack):
        #mess with the string and keep track of num flips
        #choose the top i pancakes (while the pancake is -)
        i = 0
        for pancake in pancakeStack:
            if pancake == '+':
                break
            else:
                i+=1

        #if i = 0, flip the entire stack of pancakes
        if(i == 0):
            for k in range(0, len(pancakeStack)):
                listOfPancakes1 = list(pancakeStack)
                if(listOfPancakes1[k] == '+'):
                    listOfPancakes1[k] = '-'
                else:
                    break
                pancakeStack = "".join(listOfPancakes1)
        else:
            #flip the top i pancakes
            for j in range(0,i):
                listOfPancakes2 = list(pancakeStack)
                listOfPancakes2[j] = '+'
                pancakeStack = "".join(listOfPancakes2)

        numFlips+=1

    print("Case #"+str(testCase)+": " + str(numFlips))
