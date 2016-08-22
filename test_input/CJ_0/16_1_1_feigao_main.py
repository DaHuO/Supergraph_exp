#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
from functools import wraps, lru_cache


def io_wrapper(func):
    @wraps(func)
    def _func(in_file=None, out_file=None):
        in_buffers = []
        if in_file is None:
            while True:
                try:
                    s = input()
                    if s.strip():
                        in_buffers.append(s.strip())
                except:
                    break
        else:
            with open(in_file, 'r') as f:
                in_buffers.extend([line.strip() for line in f.read().strip().splitlines()])
        assert len(in_buffers) == int(in_buffers[0]) + 1

        out_buffers = []
        for case_id, line in enumerate(in_buffers[1:], 1):
            out_buffers.append('Case #{}: {}'.format(case_id, func(line)))

        if out_file is not None and os.path.exists(out_file):
            print('Out file {} already exists!'.format(out_file), file=sys.stderr)
            out_buffers = None
        if out_file is None:
            print('\n'.join(out_buffers))
        else:
            with open(out_file, 'w') as f:
                f.write('\n'.join(out_buffers))

    return _func


@io_wrapper
@lru_cache(maxsize=None)
def solution(line_str):
    return "Answer Str"


@io_wrapper
@lru_cache(maxsize=None)
def the_last_word(line_str):
    prefix, suffix = '', ''
    for i in range(len(line_str) - 1, -1, -1):
        if line_str[i] >= max(line_str[:i + 1]):
            prefix = prefix + line_str[i]
        else:
            suffix = line_str[i] + suffix
    return prefix + suffix


if __name__ == '__main__':
    the_last_word('A-large.in.txt', 'A-large.out.txt')
