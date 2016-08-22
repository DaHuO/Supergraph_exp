import fs

def convert_to_int(input):
  if input == '+':
    return 1
  return 0

def abs_gradient(input):
  if len(input) < 2:
    return []
  grad = [0] * (len(input) - 1)
  for i, d in enumerate(input):
    if i is 0: continue
    grad[i - 1] = abs(d - input[i - 1])
  return grad

def solve(input):
  # Transform to int list
  cookies = list(map(convert_to_int, input))

  # Minimum number of flips to turn them on one side
  flips = sum(abs_gradient(cookies))

  # Now we have to check the first cookie
  # and add one more additional flip when necessary

  # when we don't have to flip
  if flips is 0:
    return 1 - cookies[0]
  elif flips % 2 is 1:
    return flips + cookies[0]
  else:
    return flips + 1 - cookies[0]

if __name__ == '__main__':
  IN_NAME = 'B-large.in'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  for i, row in enumerate(rows):
    # Skip first row (contains number of entries)
    if i == 0: continue
    # Skip last row (contains only \n)
    if i == len(rows) - 1: continue
    solution += 'Case #%i: %s\n' % (i, str(solve(row)))

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)