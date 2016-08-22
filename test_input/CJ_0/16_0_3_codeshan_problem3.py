import math
import random

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return divisor
    
    return True

def calculatenum(coin,n):
	list_eval=[];
	for i in range(2,11):		
		val=0;
		count=n-1;
		for z in xrange(0,n):
			num=int(coin[z]);
			val=val+num*(i**count);
			count=count-1;
		list_eval.append(val);
	return list_eval

def checkifvalid(coin,n):
	allbases=calculatenum(coin,n);
	factor_list=map(is_prime,allbases);
	return factor_list;

def generatenewcoin(n):
  new_coin="1"
  for x in xrange(1,n-1):
 	new_coin=new_coin+str(random.randint(0,1));
  new_coin=new_coin+"1";
  return new_coin	  
	

def main():
	final_list=[]
	factor_lists=[];

	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  n,j = [int(s) for s in raw_input().split(" ")]
	  # print n;
	  # print j;
	  
	  # n=6;
	  # j=3;
	  old_j=j;
	  coin="1"
  	  for x in xrange(1,n-1):
  	 	coin=coin+"0";
  	  coin=coin+"1";
	  while j!=0:	  	
		  factor_list = checkifvalid(coin,n); 
		  if (True not in factor_list) and (coin not in final_list):		  		  
		  	final_list.append(coin);		  	
		  	factor_lists.append(factor_list);
		  	j=j-1;
		  coin=generatenewcoin(n);		  
	  # allbases=calculatenum(coin,n)
   #    factor_list=map(is_prime,x);
	  # print factor_list
	  # final_list.append(coin);
	  # j=j-1;
	  # while (j!=0):	  	 	  	 
	  # 	 new_possiblenums=[x + y for x, y in zip(factor_list,allbases)]
	  # 	 isvalidcoin
	  # 	 j=0;
	  final_string="";
	  # print final_list;
	  # print factor_lists;
	  # print old_j;
	  for m in range(0,old_j):
	  	list_a=factor_lists[m];	  	
	  	final_string= final_string+final_list[m]+" "	  	
	  	for each_num in list_a:
	  		final_string=final_string+str(each_num)+" "
	  	final_string=final_string+"\n"

	  # print final_string;
	  
	  print "Case 1:"
	  print final_string


if __name__ == "__main__":
	main()