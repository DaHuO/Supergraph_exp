import os, re, sys
from copy import deepcopy

sys.setrecursionlimit(500000)


def make_fmt(formatter, specials):
    return lambda item: specials.get(item, formatter(item))


def make_seq_fmt(sep, item_fmt=str):
    return lambda items: sep.join([item_fmt(i) for i in items])


class ReadWrite:
    """
    Utility class for Google CodeJam.
    Handles input/output, counting and formatting cases.
    """

    def __init__(self, file_name=None, verbose=True, formatter=str):
        self.verbose = verbose
        self.formatter = formatter
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self._case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types):
        """
        Read a line from the input file.  Divide that line into
        space-separated words, use *types to convert each word in order.  If
        there are more words in the line than provided types, the last
        provided type will be used for all subsequent words.

        """
        words = self.in_file.readline().strip().split()
        if len(words) == 1:
            return types[0](words[0])
        return [types[min(i, len(types) - 1)](words[i])
                for i in range(len(words))]

    def write_case(self, output, pfx_char=' '):
        pfx = "Case #%d:" % self._case_idx
        self._case_idx += 1
        text = pfx + pfx_char + self.formatter(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


def solve(letters):
    result = [letters[0]]
    for c in letters[1:]:
        if c >= result[0]:
            result.insert(0, c)
        else:
            result.append(c)
    return ''.join(result)


if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'A-tiny-practice.in'
    rw = ReadWrite(input_name, formatter=str)
    T = rw.read_line(int)
    for t in range(T):
        S = rw.read_line(str)
        rw.write_case(solve(S))
