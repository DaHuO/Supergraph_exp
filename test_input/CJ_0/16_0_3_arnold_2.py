import random
file1 = "C-small-attempt0.in.txt"
file = open(file1, "r")
attempt = int(file.readline().strip())
print("Case #", end='')
print(1, end="")
print(": ")
data = file.readline().strip().rsplit(sep=' ')
length = int(data[0])
time = int(data[1])
already = []
right = []
def isPrime(n):    
    if n <= 1:    
        return False   
    i = 2   
    while i*i <= n:    
        if n % i == 0:    
            return False   
        i += 1   
    return True
def find_factor(x):
     find = False
     for s in range(2, int(x/2)):
          if x % s == 0:
               find = True
               return s
     if find == False:
          return 0
while(len(right) != time):
     x = list(str(bin(random.randint(2**(length - 2), 2**(length - 1) - 1))))[2::]
     x = "".join(x)
     x += '1'
     if(x in already):
          continue
     already.append(x)
     factor = []
     for i in range(2, 11):
          number = 0
          for s in range(0, len(x)):
               number += int(x[s]) * i ** (len(x) - s - 1)
          if isPrime(number) == False:
               right_factor = find_factor(number)
               factor.append(right_factor)
                
     if x not in right and len(factor) == 9:
          right.append(x)
          print(x, end  = " ")
          for i in range(0, 9):
               print(factor[i], end = ' ')
          print()
          
               
               
               
          
     
     
     
     
     

     
     
               
               
     
     
     
     
          
          
