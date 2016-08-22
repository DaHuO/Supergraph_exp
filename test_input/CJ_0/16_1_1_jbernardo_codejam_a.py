import itertools

def read_file_simple(name, fn=str):
    with open(name) as file:
        lines = iter(file)
        ncases = int(next(lines))

        return [fn(next(lines).strip()) for _ in range(ncases)]


def solve(input_file, func, read_func, stdout=False):
    input_data = read_func(input_file)

    text = '\n'.join(
        'Case #{}: {}'.format(i, func(data))
        for i, data in enumerate(input_data, 1)
    )

    if stdout:
        print(text)
    else:
        with open(input_file + '.out', 'w') as file:
            print(text, file=file)


def func_a(val):
    out, *val = val
    for c in val:
        if c >= out[0]:
            out = c + out
        else:
            out += c
    return out


if __name__ == '__main__':
    solve('tests/A-large.in', func_a, read_file_simple, False)
