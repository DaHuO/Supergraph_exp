import gcj

def solve(s):
    x = s[0]
    for c in s[1:]:
        if c >= x[0]:
            x = c + x
        else:
            x += c
    return x

if __name__ == '__main__':
    gcj.main(solve)
