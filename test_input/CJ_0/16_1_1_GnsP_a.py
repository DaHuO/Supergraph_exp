for tc in range(1, int(input())+1):
  S = input()
  R = [S[0]]
  for ch in S[1:]:
    if ch >= R[0]:
      R.insert(0, ch)
    else:
      R.append(ch)
  print('Case #{_tc}: {_sol}'.format(_tc=tc,_sol=''.join(R)))

