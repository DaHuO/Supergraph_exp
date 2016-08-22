file1 = "1.txt"
file = open(file1, "r")
attempt = int(file.readline().strip())
Attempt = 1
def pancake(x) -> int:
    global num
    i = 0
    j = i
    while(string[j] == string[j + 1]):
        j += 1
        if(j == len(x) - 1):
            return 0
    if(string[j] == '+'):
        p = j + 1
        while(p < len(string) - 1 and string[p] == string[p + 1]):
            p += 1
        for k in range(0, p + 1):
            if(string[k] == '-'):
                string[k] = '+'
            else:
                string[k] = '-'
        num += 1
        for k in range(0, j + 1):
            string[k] = '+'
        num += 1
        i = p + 1
    if(string[j] == '-'):
        for k in range(0, j + 1):
            string[k] = '+'
        num += 1
    if(i != len(string) - 1):
        return pancake(x)
    
while(Attempt <= attempt):
    print("Case #", end='')
    print(Attempt, end="")
    print(": ", end="")
    string = list(file.readline().strip())
    num = 0
    if('+' not in string):
        print(1)
        Attempt += 1
        continue
    if('-' not in string):
        print(0)
        Attempt +=1
        continue
    pancake(string)
    print(num)
    Attempt += 1

          
          
