def word(lst):
    arr = [i for i in lst]
    result = ""

    for i in arr:
        if result == "":
            result = i
        elif i >= result[0]:
            result = i + result
        else:
            result = result + i
    return result

t = int(raw_input())
for i in xrange(1, t + 1):
    n = raw_input()
    result = word(n)
    print("Case #{}: {}".format(i, result))
