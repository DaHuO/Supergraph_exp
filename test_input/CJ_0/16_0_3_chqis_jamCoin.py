import sys

# args are a string and array of strings
def printJamCoin(jamCoin, divs):
    sys.stdout.write(jamCoin)
    for i in divs:
        sys.stdout.write(' ')
        sys.stdout.write(i)
    print ''

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2: return True
  if n%2 == 0: return 2
  if n < 9: return True
  if n%3 == 0: return 3
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f += 6
  return True            
        
def main():
    N = int(sys.argv[1])
    J = int(sys.argv[2])
    print("Case #1:")
    j = 0
    for potential in xrange(2**(N-2)):
        fr = '{0:0'+str(N-2)+'b}'
        midStr = fr.format(potential)
        jc = '1' + midStr + '1'
        divisors = []
        prime = False
        for base in xrange(2, 11):
            divisor = isPrime(int(jc,base))
            if divisor is True:
                prime = True
            else:
                divisors.append(str(divisor))
        if not prime:
            printJamCoin(jc, divisors)
            j+=1
            if j == J:
                return
main()
