from __future__ import print_function
import sys
from math import sqrt; 
from itertools import count, islice
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
def warning(*objs):
	print("WARNING: ", *objs, file=sys.stderr)
def is_prime(a):
	i=2
	warning(a)
	while i*i<=a:
		if a%i == 0:
			return False
		i=i+1
	return True
def dividor(a):
	i=2
	while i*i<=a:
		if a%i == 0:
			return i
		i=i+1
	return True
def dec_to_bin(x):
	return (bin(x)[2:])

T=int(raw_input())
@timeout(1)
def go(count,Ab,A):
	if not is_prime(A) and not is_prime(int(Ab,3)) and not is_prime(int(Ab,4)) and not is_prime(int(Ab,5)) and not is_prime(int(Ab,6)) and not is_prime(int(Ab,7)) and not is_prime(int(Ab,8)) and not is_prime(int(Ab,9)) and not is_prime(int(Ab,10)):
		print(Ab+" "+str(dividor(A))+" "+str(dividor(int(Ab,3)))+" "+str(dividor(int(Ab,4)))+" "+str(dividor(int(Ab,5)))+" "+str(dividor(int(Ab,6)))+" "+str(dividor(int(Ab,7)))+" "+str(dividor(int(Ab,8)))+" "+str(dividor(int(Ab,9)))+" "+str(dividor(int(Ab,10))))
		count=count+1
		warning(count)
	return count
for i in range(1,T+1):
	s=raw_input().split()
	N=int(s[0])
	J=int(s[1])
	print("Case #"+str(i)+":")
	count=0
	A=1<<(N-1)|1
	while A <(1<<N):
		Ab=dec_to_bin(A);
		warning(Ab)
		try:
			count=go(count,Ab,A)
		except TimeoutError:
			pass
		if count==J:
			break;
		A=A+0b10
