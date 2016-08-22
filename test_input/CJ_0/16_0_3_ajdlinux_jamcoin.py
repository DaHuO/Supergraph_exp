#!/usr/bin/env python3

# Code Jam 2016 - Qualification Round - Problem C
# Copyright (C) 2016 Andrew Donnellan

import sys

from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

inp = [int(x) for x in sys.stdin.readlines()[1].split()]

@timeout(3)
def prove_jamcoin(jamcoin):
    interpretations = [int(jamcoin, n) for n in range(2,11)]
    divisors = []
    for i, interpretation in enumerate(interpretations):
        divisor = None
        for j in range(2, interpretation // 2):
            if interpretation % j == 0:
                divisor = j
                break
        if not divisor:
            #print("No divisor for " + str(interpretation))
            raise Exception
        else:
            divisors.append(divisor)
    return divisors

jamcoins = []
count = 0
while len(jamcoins) < inp[1]:
    jamcoin = "1" + bin(count)[2:].zfill(inp[0] - 2) + "1"
    #print("Proving jamcoin " + jamcoin)
    try:
        jamcoins.append((jamcoin, prove_jamcoin(jamcoin)))
    except (Exception, TimeoutError):
        pass
    count += 1

print("Case #1:")
for (jamcoin, proof) in jamcoins:
    print("{} {}".format(jamcoin, " ".join([str(p) for p in proof])))
