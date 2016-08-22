import sys

def memoize(func):
    _cache = {}

    def _inner(*args, **kwargs):
        joined = ''.join([str(args), str(kwargs)])
        if joined not in _cache:
            _cache[joined] = func(*args, **kwargs)
        return _cache[joined]
    return _inner


@memoize
def _game(result, word, i):

    if i == len(word):
        return result
    pre = ''.join([word[i], result])
    post = ''.join([result, word[i]])
    if i == len(word) - 1:
        return max(pre, post)
    return max(_game(pre, word, i+1), _game(post, word, i+1))

def solve(word):
    sorted_ = sorted(word)
    reversed_ = reversed(word)
    if sorted_ == word:
        return reversed_
    elif sorted_ == reversed_:
        return word
    return _game(word[0], word, 1)


def read_input_and_solve(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if not i:
                T = int(line.strip())
            else:
                word = line.strip()
                # only print 1 case here
                print "Case #{}: {}".format(i, solve(word))


if __name__ == '__main__':
     if len(sys.argv) > 1:
         f = sys.argv[1]
     else:
         raise Exception('Must have input file')
     try:
         read_input_and_solve(f)
     except IOError:
         print "Unable to read file!"



