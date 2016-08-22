"""def flip(stack,place):
    newvar=""
    for i in range(place,-1,-1):
        newvar += "+" if stack[i] =="-" else "-"
    newvar += stack[place+1::]
    return newvar

def findfirst(stack):
    possibility,searching,count = set(stack),"+"*len(stack),0
    possibility.add(stack)
    while searching not in possibility:
        newset = set()
        for candidate in possibility:
            for index in range(len(candidate)):
                newset.add(flip(candidate,index))
                print(flip(candidate,index))
        possibility = newset
        count += 1

    return count
"""


def findfirst2(stack):
    searching,count = "+"*len(stack),0
    while stack != searching:
        for i in range(len(stack)-1,-1,-1):
            if stack[i] == "-":
                var = ""
                for i in range(i+1):
                    var += "+" if stack[i] == "-" else "-"
                var += stack[i+1::]
                stack = var
                break
        count += 1
    return count

for i in range(1,int(input())+1):
    print("Case #{}: {}".format(i, findfirst2(input())))


