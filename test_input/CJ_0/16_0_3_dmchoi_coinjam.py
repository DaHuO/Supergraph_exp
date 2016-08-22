
if __name__== "__main__":
  T = int(raw_input());
  for t in range(T):
    (N,J) = [int(i) for i in raw_input().strip().split(" ")]
    print "Case #{}:".format(t+1)
    for i in range(J):
      s = '1{}1'.format(bin(i)[2:].zfill(N/2-2))
      ans = ""
      for d in range(2,11):
        ans += str(1+pow(d,N/2)) + " "
      print s*2 + " " + ans
