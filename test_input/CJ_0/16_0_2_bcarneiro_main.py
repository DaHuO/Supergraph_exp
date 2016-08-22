def solve(line):
  i = 0
  # print line
  while True:
    initial = line[0]
    j = 0
    for c in line:
      if line[j] != initial:
        line = line[j] * j + line[j:]
        i+=1
        # print line
        break
      j += 1
    if j == len(line):
      # reached end and it's all the same
      if line[j-1] == '-':
        return i+1
      else:
        return i

if __name__ == "__main__":
  n = input()

  for i in xrange(1, n+1):
    line = raw_input()
    print("Case #{0}: {1}".format(i, solve(line)))
