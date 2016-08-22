
INPUT_FILE = 'A-large.in';
OUTPUT_FILE = 'A-small-practice.out';

def algorithmA(N):
   digits = [False,False,False,False,False,False,False,False,False,False]
   count = 1
   lastNumber = N;

   if N == 0:
      return "INSOMNIA"

   while not all(digits):
      lastNumber = N*count
      tokens = map(int,list(str(lastNumber)))
      print tokens
      for token in tokens:
         digits[token] = True
      count +=1

   return str(lastNumber)

def solve(data):
   N = int(data[0])
   return str(algorithmA(N));

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(1,len(lines)):
      result = solve([lines[i]])
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()