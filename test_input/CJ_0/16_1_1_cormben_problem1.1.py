import q
import sys; sys.setrecursionlimit(150000)


def _strip_data(data):
    return [x.strip() for x in data.readlines()[1:]]


def _write_output(completed_data, out_file):
    out_lines = ['Case #{}: {}\n'.format(i+1, line) for i, line in enumerate(completed_data)]
    out_file.writelines(out_lines)


def coding_challenge_specific_io(challenge_function):
    with open('input') as in_file:
        parsed_data = _parse_data(_strip_data(in_file))
    completed_data = [challenge_function(data) for data in parsed_data]
    q(completed_data)
    with open('output', 'w') as out_file:
        _write_output(completed_data, out_file)


@q
def _parse_header(header_line):
    header_data = header_line.split()
    header = {'end_line':0, 'data':header_data}
    return header


@q
def _parse_line(line):
    return [int(x) for x in line.split()]


def _parse_data(in_lines):
    if not in_lines: 
        return []
    header = _parse_header(in_lines[0])
    end = header['end_line']
    single_test = [_parse_line(line) for line in in_lines[1:end+1]]
    remaining_parsed_data = _parse_data(in_lines[end+1:])
    return [{'header':header, 'data':single_test}] + remaining_parsed_data


def func(data):
    word = data['header']['data'][0]
    new_word = [word[0]]
    if len(word) > 1:
        for x in word[1:]:
            if x >= new_word[0]:
                new_word = [x] + new_word
            else:
                new_word = new_word + [x]
    return ''.join(new_word)



if __name__=='__main__':
    #example
    coding_challenge_specific_io(func)


