# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
  # n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    string =  [s for s in input()] 
    result = []
    i=0
    while i < len(string):
        current_max=ord(max(result)) if len(result)>0 else 0
        # print(current_max)
        # print("ord"+str(ord(string[i])))
        if ord(string[i]) >= current_max:
            result.insert(0, string[i])
        elif ord(string[i]) < current_max:
            result.append(string[i])
        # print(result)
        i+=1        


    print("Case #{}: {}".format(j, "".join(result)))
  # check out .format's specification for more formatting options