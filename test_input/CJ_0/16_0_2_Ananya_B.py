import fileinput

case = -1
for line in fileinput.input():
  line = line.strip(' \t\n\r')
  case += 1
  if case == 0:
    continue
  line += '+'
  differences = 0
  for i in range(len(line)-1):
    if line[i] != line[i+1]:
      differences += 1
  print("Case #%d: %d" % (case, differences))
