import sys, itertools

def last2(word):

    keywords = list(map("".join, itertools.permutations(word)))

    result = ""

    for i in keywords:
        if i >= result:
            result = i

    return result

def last(word):

    result = word[0]

    for letter in word[1:]:
        if(result + letter) > (letter + result):
            result += letter
        else:
            result = letter + result

    return result

if __name__ == "__main__":
    f = sys.stdin
    t = int(f.readline())
    arr = dict()
    for i in range(1,t+1):
        line = f.readline().strip()
        arr[i] = last(line)
    for j in arr:
            print("Case #%d: %s" % (j,arr[j]))


##if __name__ == "__main__":
##    f = sys.stdin
##    t = int(f.readline())
##    arr = dict()
##    for i in range(1,t+1):
##        line = f.readline().strip()
##        arr[i] = pancakes(line)
##    for j in arr:
##        print("Case #%d: %d" % (j,arr[j]))


##if __name__ == "__main__":
##    f = sys.stdin
##    t = int(f.readline())
##    arr = dict()
##    for i in range(1,t+1):
##        line = f.readline().strip().split()
##        arr[i] = makeJam(int(line[0]),int(line[1]))
##    for j in arr:
##        print("Case #%d:" % (j))
##        for k in arr[j]:
##            print(k)
