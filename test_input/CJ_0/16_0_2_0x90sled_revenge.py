import fileinput


def pancakes_happy(stack):
    def flip(stack):
        return ['-' if i == '+' else '+' for i in stack[::-1]]

    st = list(stack)
    i = 0
    while '-' in st:
        flip_index = max(st.index('-'), st.index('+') if '+' in st else len(st))
        st = flip(st[:flip_index]) + st[flip_index:]
        i += 1
    return i


def main():
    lines = [line.strip() for line in fileinput.input()][1:]

    for case, stack in enumerate(lines, 1):
        print "Case #{case}: {flips}".format(case=case, flips=min(pancakes_happy(stack),
                                                                  pancakes_happy(stack[::-1]) + 1))


if __name__ == '__main__':
    main()
