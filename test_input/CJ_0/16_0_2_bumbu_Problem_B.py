import string

_file = open("./B-large.in")
# _file = open("./B-small-attempt1t.in")
_result = open("./result.txt", "w")

datasetSize = int(_file.readline())

for i in range(datasetSize):
  symbols = _file.readline().replace("\n", "")
  deduped = []

  for symbol in symbols:
    if len(deduped) == 0 or deduped[-1] != symbol:
      deduped.append(symbol)

  # print symbols
  # print deduped
  operations = 0
  for j, value in enumerate(deduped):
    if value == "-":
      if j == 0:
        operations += 1
      else:
        operations += 2

  result = "Case #" + str(i + 1) + ": " + str(operations)

  print result
  _result.write(result + "\n")

_file.close()
_result.close()
