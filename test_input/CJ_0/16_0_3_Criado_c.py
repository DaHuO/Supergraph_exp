line=input(); line=input()
n=int(line.split()[0]); j=int(line.split()[1])

print("Case #1:")
for i in range(0,j):
  print("11",bin(i)[2:].zfill((n//2)-2).replace("0","00").replace("1","11"),"11 3 4 5 6 7 8 9 10 11", sep='')
