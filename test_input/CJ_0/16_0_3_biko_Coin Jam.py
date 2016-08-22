
# coding: utf-8

# In[1]:

import itertools
import io
import math
from concurrent.futures import ThreadPoolExecutor
from collections import namedtuple


# In[2]:

TEST_INPUT = """1
6 3"""


# In[3]:

SMALL_INPUT = """1
16 50"""


# In[4]:

LARGE_INPUT = """1
32 500"""


# In[5]:

def divisors(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            yield i
            if i != number // i:
                yield number // i


# In[6]:

def is_prime(number):
    if number <= 1:
        return False
    
    try:
        next(divisors(number))
    except StopIteration:
        return True
    else:
        return False


# In[7]:

class Case(namedtuple("Case", ("length", "count"))):
    def __new__(cls, line):
        return super().__new__(cls,
                               *(int(s) for s in line.split()))


# In[8]:

def get_cases(data):
    with io.StringIO(data) as stream:
        num_cases = int(stream.readline())
        assert num_cases == 1
        yield from map(Case, stream)


# In[9]:

def interpretations(maybe_coin):
    yield from (int(maybe_coin, base=base)
                for base
                in range(2, 11))


# In[10]:

def is_jamcoin(maybe_coin):
    if maybe_coin[0] != "1" or maybe_coin[-1] != "1":
        return False
    
    for interpretation in interpretations(maybe_coin):
        if is_prime(interpretation):
            return False
        
    return True


# In[11]:

def all_jamcoins_of_length(length):
    maybe_coins = map(lambda x: "".join(x), itertools.product(("0", "1"), repeat=length))
    yield from filter(is_jamcoin, maybe_coins)


# In[12]:

def all_divisors_of_coin(coin):
    yield from map(lambda x: next(divisors(x)), interpretations(coin))


# In[13]:

def solve_case(case):
    coins = itertools.islice(all_jamcoins_of_length(case.length), case.count)
    return tuple((coin, tuple(all_divisors_of_coin(coin)))
                 for coin in coins)


# In[14]:

with ThreadPoolExecutor() as executor:
    for index, solution in enumerate(executor.map(solve_case, get_cases(SMALL_INPUT)), start=1):
        print("Case #{}:".format(index))
        for coin, divisors in solution:
            print("{} {}".format(coin, " ".join(str(x) for x in divisors)))


# In[ ]:



