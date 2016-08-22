import sys

def main():
    data = sys.stdin.readlines()
    for i in range(1, len(data)):
        print("Case #" + str(i) + ": " + str(solve(data[i])))

def solve(s):
    res = ''
    for i in range(len(s)):
        if not res:
            res = res + s[0]
        else:
            first = res[0]
            if s[i] < first:
                res = res + s[i]
            else:
                res = s[i] + res
    return res
    
    


if __name__ == "__main__":
    main()
