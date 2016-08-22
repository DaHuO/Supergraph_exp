# A.py
# jreiter

for tc in range(int(input())):
  S = input()
  word = ""
  for ch in S:
    if word == "":
      word = ch
    else:
      word = word + ch if ch < word[0] else ch + word

  print("Case #{}: {}".format(tc+1, word))