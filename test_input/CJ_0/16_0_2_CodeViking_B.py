import os, re, sys

sys.setrecursionlimit(500000)


class ReadWrite:
    def __init__(self, file_name=None, verbose=True):
        self.verbose = verbose
        if file_name is None:
            self.in_file = sys.stdin
            self.out_file = sys.stdout
        else:
            self.in_file = open(file_name)
            self.out_file = open(os.path.splitext(file_name)[0] + '.out', 'w')
        self.case_idx = 1

    def msg(self, output, end='\n'):
        sys.stderr.write(str(output) + end)

    def read_line(self, *types, all=None):
        words = self.in_file.readline().strip().split()
        if all is not None:
            return [all(w) for w in words]
        if len(types) == 0:
            return words
        assert (len(words) == len(types))
        if len(types) == 1:
            return types[0](words[0])
        return [t(w) for t, w in zip(types, words)]

    def write_case(self, output, true="YES", false="NO", join='\n'):
        pfx = "Case #%d:" % self.case_idx
        self.case_idx += 1
        if isinstance(output, list):
            text = join.join([pfx] + output)
        elif isinstance(output, bool):
            text = pfx + ' ' + (true if output else false)
        else:
            text = pfx + ' ' + str(output)
        self.out_file.write(text + '\n')
        if self.verbose:
            self.msg(text)
        else:
            self.msg(pfx)


upside_down_stack = re.compile(r'\-+')
finished_stack = re.compile(r'\++')


def solve(stack):
    if upside_down_stack.fullmatch(stack):
        return 1
    if finished_stack.fullmatch(stack):
        return 0

    m = upside_down_stack.match(stack)
    if m:
        s = ('+' * m.end()) + stack[m.end():]
        return solve(s) + 1
    m = finished_stack.match(stack)
    if m:
        s = ('-' * m.end()) + stack[m.end():]
        return solve(s) + 1
    assert (False)


if __name__ == '__main__':
    input_name = sys.argv[1] if len(sys.argv) > 1 else 'B-tiny-practice.in'
    rw = ReadWrite(input_name)
    T = rw.read_line(int)
    for t in range(T):
        S = rw.read_line(str)
        rw.write_case(str(solve(S)))
