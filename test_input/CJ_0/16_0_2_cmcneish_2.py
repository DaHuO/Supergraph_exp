def flip(string, index):
    flipped = string[:index+1][::-1]
    flipped = flipped.replace("-", "*")
    flipped = flipped.replace("+", "-")
    flipped = flipped.replace("*", "+")
    return flipped + string[index+1:]

def min_flips(string):
    flips = 0
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            string = flip(string, i)
            flips += 1
    if string[len(string)-1] == "-":
        #probably unnecessary
        string = flip(string, len(string)-1)
        flips += 1
    return flips

test_count = int(input())
for i in range(test_count):
    i += 1
    print("Case #"+str(i)+": " + str(min_flips(input())))
