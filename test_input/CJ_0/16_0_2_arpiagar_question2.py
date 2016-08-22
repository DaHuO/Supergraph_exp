# # --+-
#   +-++
#   --++
#   + + + - + -
#   - - - - + -
#   + - + + + + 


def convert_to_plus(input1):
  input_list = []
  counter = 0
  for i  in xrange(0,len(input1)):
    input_list.append(input1[i])
  while True:
    flag = False
    flag1 =  False
    first_negative_index =  None
    for index,elem in reversed(list(enumerate(input_list))):
      #import pdb;pdb.set_trace()
      if elem == '-' and flag == False:
        if index == 0:
          return counter+1
        flag = True
        first_negative_index =  index
        i = 0
        while input_list[i] == '+':
          input_list[i] = '-'
          i += 1
          flag1 =  True
      if flag1:  
        counter += 1
        break
      elif elem == '-' and flag == True:
        input_list = swap_index(input_list,-1,first_negative_index)
        counter += 1
        break
      if index == 0 and flag == False:
        return counter
      if index == 0 and flag == True:
        input_list = swap_index(input_list,-1,first_negative_index-1)
        


def swap_index(input_list, start, end):
  temp_list = []
  for i in xrange(end, start, -1):
    if input_list[i] == '+':
      temp_list.append('-')
    else:
      temp_list.append('+')
  return temp_list+input_list[end+1:len(input_list)]







if __name__ == "__main__":
  filepath = raw_input().strip()
  f = open(filepath, 'rb')
  out  =  open('output.txt','wb')
  flag = True
  for lines in f:
    if flag:
      n =  lines
      flag = False
      count = 1
      continue
    elem =  lines.strip()
    print "elem:"+elem
    out.write("Case #"+str(count)+": "+str(convert_to_plus(elem)))
    out.write('\n')
    count += 1
  out.close()
  f.close()

# -
# + - 
# + - + - + +

# - - + - + +
# + - + + + +
# - - + + + +
# + + + + + +

# + - + - + +
#   # - - + -
#     + - + +
#     - - + +
#     + + + + 

#     - - + - + -

#      - + + - +
#      + - - + +
#      - + + + +
#      + + + + +
