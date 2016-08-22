
def test(test_idx, inp):
    res = ''
    left = []
    right = []
    sd = sorted(inp,reverse=True)
    idx = 0
    for c in reversed(inp):
        last_char = sd[0]
        if c == last_char:
            left.append(c)
            sd.pop(0)
        else:
            right.append(c)
            sd.pop(sd.index(c))
    output = ''.join(left)+''.join(reversed(right))
    print("Case #{}: {}".format(test_idx, output))

def main():
    test_num = int(input())
    for test_idx in range(test_num):
        test(test_idx+1, input())

if __name__ == '__main__':
    main()
