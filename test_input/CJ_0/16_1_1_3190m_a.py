# -*- coding: utf-8 -*-

# Round 1A 2016
# Problem A. The Last Word

T = int(input())
Ss = [input() for i in range(T)]



for i in range(T):
  S = Ss[i]

  sp = list(S)
  a = ""

  for j in range(len(sp)):
    ap = "{}{}".format(a, sp[j])
    af = "{}{}".format(sp[j], a)
    if ap > af:
      a = ap
    else:
      a = af

  print("Case #{}: {}".format(i + 1, a))
