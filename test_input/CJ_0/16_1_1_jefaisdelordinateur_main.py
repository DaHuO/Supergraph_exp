T = int(input())  # read a line with a single integer

for case in range(1, T + 1):
        print("Case #{}: ".format(case), end="")
        string = input()
        result = string[0]
        for c in string[1:]:
            if c >= result[0]:
                result = c + result
            else:
                result = result + c;
        print(result)
