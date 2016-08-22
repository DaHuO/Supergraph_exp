import os
import re
import math
import time
import itertools
import functools
import collections
from contextlib import contextmanager


class Solver:

    def __init__(self):
        self.dir = os.path.dirname(os.path.realpath(__file__))
        self.inputs_dir = os.path.join(self.dir, 'inputs')
        self.outputs_dir = os.path.join(self.dir, 'outputs')

    def test_sample(self):
        in_file = self._select_input_file("sample")
        out_file = self._corresponding_output_file(in_file)

        result = self._solve_file(in_file)
        expected = self._read_file(out_file)

        self._compare(result, expected)

    def solve_small(self):
        in_file = self._select_input_file("small")
        out_file = self._corresponding_output_file(in_file)

        start = time.process_time()
        result = self._solve_file(in_file)
        end = time.process_time()

        self._write_file(out_file, result)

        print("\n[SUCCESS] Small input solved in %.02fs.\n" % (end - start))

    def solve_large(self):
        in_file = self._select_input_file("large")
        out_file = self._corresponding_output_file(in_file)

        start = time.process_time()
        result = self._solve_file(in_file)
        end = time.process_time()

        self._write_file(out_file, result)

        print("\n[SUCCESS] Large input solved in %.02fs.\n" % (end - start))

    @contextmanager
    def _mocking_io(self, lines=None, out=None):
        global input
        global print
        try:
            if lines is not None:
                input = iter(lines).__next__
            if out is not None:
                print = out.append
            yield out
        finally:
            input = __builtins__.input
            print = __builtins__.print

    def _compare(self, firsts, seconds):
        if isinstance(firsts, str):
            firsts = firsts.splitlines()
        if isinstance(seconds, str):
            seconds = seconds.splitlines()

        success = True

        for f, s in zip(firsts, seconds):
            if f != s:
                success = False
                print("[ERROR] %s != %s" % (f, s))

        if success:
            print("\n[SUCCESS] Good news: your solution seems correct!\n")
        else:
            print(
                "\n[FAILURE] Your solution does not provide expected output.\n"
            )

    def _select_input_file(self, keyword):
        content = os.listdir(self.inputs_dir)
        files = []
        for cont in content:
            cont_path = os.path.join(self.inputs_dir, cont)
            if (os.path.isfile(cont_path) and
                    keyword.lower() in cont.lower() and
                    cont.endswith(".in")):
                files.append(cont)

        if not files:
            raise ValueError("No input file with \"%s\" found" % keyword)

        latest = max(
            files,
            key=lambda f: [int(d) for d in re.findall('\d+', f)]
        )
        latest_path = os.path.join(self.inputs_dir, latest)

        return latest_path

    def _corresponding_output_file(self, input_file):
        base = os.path.basename(input_file)
        filename, ext = os.path.splitext(base)
        output_filename = filename + ".out"
        output_file = os.path.join(self.outputs_dir, output_filename)
        return output_file

    def _read_file(self, file):
        with open(file, 'r') as f:
            lines = f.read().splitlines()
        return lines

    def _write_file(self, file, text):
        with open(file, 'w') as f:
            f.write(text)

    def _format_output(self, outs):
        output = ""
        for i, out in enumerate(outs):
            case = "Case #%d:" % (i + 1)
            if len(out) == 1:
                case += " %s\n" % str(out[0])
            else:
                case += "\n"
                for o in out:
                    case += "%s\n" % str(o)
            output += case
        return output

    def _solve_file(self, file):
        lines = self._read_file(file)
        with self._mocking_io(lines):
            cases = self._parse(lines)

        outs = []
        for case in cases:
            out = []
            with self._mocking_io(case, out):
                self._solve(case)
            outs.append(out)

        output = self._format_output(outs)
        return output

    def _parse(self, lines):
        nb_lines = len(lines)
        n = int(lines[0])
        length = (nb_lines - 1) // n
        cases = [lines[i:i + length] for i in range(1, nb_lines, length)]
        return cases

    def _solve(self, lines):
        pancakes = list(input())
        times = 0
        while any(x == "-" for x in pancakes):
            top = pancakes[0]
            for i, p in enumerate(pancakes):
                if p != top:
                    break
                else:
                    pancakes[i] = "+" if top == "-" else "-"
            times += 1
        print(times)


solver = Solver()

solver.solve_large()
