


f = open('pancakes.in', 'r')



output = ""


for i in range(int(f.readline())):
    data = f.readline()
    counter = 0
    previous = False
    if data[0] == "-":
        counter += 1
    for pancake in data:
        if pancake == "-" and previous == "+":
            counter +=2
        previous = pancake
        
            
            

    output += "Case #" + str(i+1) + ": " + str(counter) + "\n"


