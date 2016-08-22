import sys


def main():
	# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
 	# script,filename=argv;
 	# file=open(filename)
 	# print file.read()

	t = int(raw_input())  # read a line with a single integer
	for i in xrange(1, t + 1):
	  file_read = [str(s) for s in raw_input().split(" ")]
	  sides=["+","-"]
	  pancakes = file_read[0];
	  count=0;
	  done=False;
	  while not done:
		  if "-" not in pancakes:
		  	done=True;
		  else:
		  	firstcakeside=pancakes[0];
		  	sides.remove(firstcakeside)
		  	other_side=sides[0];
		  	sides=["+","-"]
		  	# print pancakes
		  	list_split=pancakes.split(other_side,1)
		  	# print list_split
		 	to_flip=list_split[0];
		 	length_stack=len(to_flip);
		 	flipped=""
		 	for index in xrange(0,length_stack):
		 		flipped=flipped+other_side;

		  	if (len(list_split)>1):
		  		new_pancake=flipped+other_side+list_split[1];
		  	else:
		  		new_pancake=flipped+other_side

		  	pancakes=new_pancake
		  	count=count+1;

	  print "Case #{}: {}".format(i,count)
	  # check out .format's specification for more formatting options

if __name__ == "__main__":
	main()