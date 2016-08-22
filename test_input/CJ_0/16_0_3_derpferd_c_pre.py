import time
import cPickle as pickle

a = time.time()


primes = set(range(2,100))
for n in [2]+range(3,100/2,2): primes -= set(range(2*n,100,n))

print primes
# pickle.dump(primes, open("p2.obj", "wb"))

print time.time()-a