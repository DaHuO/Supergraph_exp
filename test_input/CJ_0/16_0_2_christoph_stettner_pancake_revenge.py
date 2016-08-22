
def flip_stack(stack, flip_position):
  # print "flip pos: " + str(flip_position)
  # print "before flipping: " + str(stack)
  i = 0
  stack_reversed = []
  while i <= flip_position:
    x = stack.pop(0)
    if x == '-':
      x = '+'
    elif x == '+':
      x = '-'
    stack_reversed = [x] + stack_reversed
    # print stack_reversed
    i += 1
  stack = stack_reversed + stack

  # print "after flipping: " + str(stack)
  return stack

def calc(testcase, stack):
  no_of_flips = 0
  i = 0
  while 1:
    i += 1

    # flip elements from beginning to first +
    try:
      first_occurence = stack.index('-')
      # print first_occurence
    except:
      # no - in stack, finished.
      print "not found"
      output =  "Case #" + str(testcase) + ": " + str(no_of_flips) + "\n"
      output_file.write(output)
      return

    # wenn 1. element '-' ist
    if first_occurence == 0:
      pos_last_minus = 0
      # for i, e in reversed(list(enumerate(a))):
      #...     print i, e
      # print "stack: " + str(stack)
      for index, elem in reversed(list(enumerate(stack))):
        # print index, elem
        if elem == '-':
          pos_last_minus = index
          break
      stack = flip_stack(stack, pos_last_minus)
      no_of_flips += 1
    else:
      stack = flip_stack(stack, first_occurence - 1)
      no_of_flips += 1







input_file = open('/Users/cstettner/Projects/code-jam/2016/pancake_revenge/pancake_revenge_large.in', 'r')
output_file = open('/Users/cstettner/Projects/code-jam/2016/pancake_revenge/pancake_revenge_large.out', 'w')

no_test_cases = input_file.readline()
testcase = 1

for tc in range(1, int(no_test_cases) + 1):
  stack = list(input_file.readline())
  stack.pop()
  #print stack
  calc(testcase, stack)
  testcase += 1
