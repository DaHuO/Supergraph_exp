def max_lexicographical(string):
    result = [string[0]]
    for c in string[1:]:
        if c >= result[0]:
            result = [c] + result
        else:
            result = result + [c]
    return ''.join(result)


T = int(input())
for t in range(1, T + 1):
    string = input()
    print('Case #{}: {}'.format(t, max_lexicographical(string)))