import sys
import math

def generate_jamcoins( S ):
  # set length N
  N = int(S[0])
  # set number of distinct coins J
  J = int(S[1])
  coins = []
  # initialize coin representation as list of bits
  C = '1' + '0' * (N-2) + '1'
  c = str(C)
  bases = [b for b in range(2,11)]
  # loop through valid coin count
  j=0
  while j < J:
    # iterate jamcoin: (c +=2 ) in binary representation
    c = bin( int(c, 2) + 2)[2:]
    # convert to decimal value for base 2-10
    vals = [ int(c, base) for base in bases]
    divisors = []
    for base, val in zip(bases, vals):
      for divisor in range(2, int(math.floor(math.sqrt(val)) + 1) ):
        # if value is composite, save divisor and skip to next base
        if val % divisor == 0:
#          print c, base, val, divisor
          divisors.append(divisor)
          break
      # if no divisor found, skip (break) to next valid coin value
      else:        
#        print c, base, val, "No divisor found"
        break
    # if value is composite for all bases, add coin data to coins
    else:
      coin = [ int(c) ]
      coin.extend([d for d in divisors])
      coins.append( coin )
      print coin 
#      coins.append( (c, divisors) )
      j += 1
#  print coins
  return coins

# get input filename from first arg
in_path = sys.argv[1]
# read input text file to list of strings, 1 per line
with open(in_path, 'r') as in_file:
  in_list = in_file.read().splitlines()

# convert strings to ints (and skip first string)
in_list = [s.split(' ') for s in in_list[1:] ]

#print in_list

out_list = [ generate_jamcoins(s) for s in in_list ]

for i in range(0, len(out_list)):
  print 'Case #{}:'.format(i+1)
  for x in out_list:
    for coin in x:
      print '{} {} {} {} {} {} {} {} {} {}'.format(*coin)

# 2^14 =      16384
# 2^30 = 1073741824
