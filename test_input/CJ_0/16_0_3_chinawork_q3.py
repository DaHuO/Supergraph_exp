__author__ = 'zfeng'

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return 2
  if n < 9: return True
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return f + 2
    f +=6
  return True

def validate(s):

    data = []
    vals = []
    for i in xrange(2, 11):
        val = int(s, i)
        vals.append(val)
        t = is_prime(val)
        if t == True:
            return False
        else:
            data.append(t)
    return data,vals

def solver(n, j):
    curS = '1' + '0' * (n - 2) + '1'
    mulS = '1' + '0' * 15 + '1'
    cur = int(curS, 2)
    mul = int(mulS, 2)
    count = 0
    while count < j:
        res = validate(curS)

        if res != False:
            print "{0:b}".format(cur * mul),
            for k in res[0]:
                print k,
            print ''
            count += 1
        cur += 2
        curS = "{0:b}".format(cur)

if __name__ == '__main__':
    print 'Case #1:'
    solver(16, 500)


