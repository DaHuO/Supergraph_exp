def countFlips(pans):
  count = 0
  while len(pans) != 0:
    #print pans
    if pans[0] == 1:
      pans = pans[1:]
      continue
    elif pans[0] == 0 and pans[-1] == 1:
      backindex = -1
      while pans[backindex] == 1:
        pans[backindex] = 0
        backindex-=1

      count += 2
      pans = flip(pans)

    elif pans[0] == 0:
      count += 1
      pans = flip(pans)
      continue
    else:
      print "the hell"
  return count

def flip(arr):
  old = arr[:]
  out = []
  for i in range(len(old)):
    if old[i] == 1 :
      out.append(0)
    else:
      out.append(1)

  return out[::-1]

def toIntArray(pans):
  out = []
  for c in pans:
    if c == "-":
      out.append(0)
    elif c == "+":
      out.append(1)
  return out

fname = "2.txt"
with open(fname) as f:
  body = f.readlines()

t = int(body[0])

body = body[1:]

for i in range(t):
  line = toIntArray(body[i])[::-1]
  print "Case #%d: %s" % (i+1, countFlips(line))
