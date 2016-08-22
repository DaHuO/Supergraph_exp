#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

t = int(input()) # Number of test cases

for i in range(t):
    s = input()
    last_word = s[0]
    for j in range(1, len(s)):
        last_word = sorted([s[j] + last_word, last_word + s[j]])[-1] # Sort each time and take the last one
    print("Case #{}: {}".format(i + 1, last_word))
