

def process(string):
    maxchar = max(string)
    result = string[0]
    start = end = result
    for ch in string[1:]:
        if ch >= start:
            start = ch
            result = ch + result
        else:
            end = ch
            result += ch
    return result 
        


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        print("Case #" + str(i+1) + ": " + process(input().strip()))
