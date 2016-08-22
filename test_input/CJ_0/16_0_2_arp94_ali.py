import sys


def main():

	t = int(raw_input())  # read a line with a single integer
	for i in range(1, t + 1):
	  file_read = [str(s) for s in raw_input().split(" ")]
	  sides=["+","-"]
	  pancakes = file_read[0];
	  count=0;
	  done=0;
	  while not done:
		  if "-" in pancakes:
		  	firstcakeside=pancakes[0];
		  	sides.remove(firstcakeside)
		  	other_side=sides[0];
		  	sides=["+","-"]
		  	list_split=pancakes.split(other_side,1)
		 	to_flip=list_split[0];
		 	length_stack=len(to_flip);
		 	flipped=""
		 	for index in range(0,length_stack):
		 		flipped=flipped+other_side;
		  	if (len(list_split)<1):
		  		new_pancake=flipped+other_side
		  	else:
		  		new_pancake=flipped+other_side+list_split[1];	  		

		  	pancakes=new_pancake
		  	count+=1;

		  else:
		  	done=1;

		  	
	  print "Case #{}: {}".format(i,count)
	  # check out .format's specification for more formatting options

if __name__ == "__main__":
	main()