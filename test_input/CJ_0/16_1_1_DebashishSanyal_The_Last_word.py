t = int(raw_input())

result = ""
for i in xrange(1, t + 1):
  n =  str(raw_input())
  current = ""
  for char in n:
      if current == "":
          current += char
      elif char >= current[0]:
          current = char + current
      else:
          current = current + char
  result =  result + "Case #{}: {}\n".format(i, current)
  #print n

file_name = "output.txt"
text_file = open(file_name, "w")
text_file.write(result)
