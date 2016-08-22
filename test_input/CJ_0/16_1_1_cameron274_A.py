def run_test():
    s = raw_input()
    result = ""
    result = result + s[0]
    for char in s[1:]:
        if char >= result[0]:
            result = char + result
        else:
            result = result + char
    return result

t = int(raw_input())
for i in range(1, t+1):
    print("Case #%d: %s" % (i, run_test()))