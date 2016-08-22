thelist = []
thechar = ""
poppedchar = ""
count = 0

def flip(input_string):
    global thelist, thechar, poppedchar, count
    thelist = list(input_string) # turn string into array of chars
   
    thechar = thelist.pop(0) # pop first char in list
    poppedchar = thechar

    for char in range(0, len(thelist)):
        poppedchar = thelist.pop(0)
        if thechar == poppedchar:
            continue # same char
        else: # change occurred
            count += 1
            thechar = poppedchar
            
    if poppedchar == "-": # one last flip
        count += 1

    return count

def reset():
    global thelist, thechar, poppedchar, count
    thelist = []
    thechar = ""
    poppedchar = ""
    count = 0

def start(input_string):
    return flip(input_string)

infile = open('B-large.in','r')
cases = int(infile.readline())

outfile = open("B-large.out", "w")
for case in range(1, cases + 1):
    input_string = infile.readline().rstrip('\n') # REMOVE new line char!!
    outfile.write("Case #" + str(case) + ": " + str(start(input_string)) + '\n')
    reset()

outfile.close()
