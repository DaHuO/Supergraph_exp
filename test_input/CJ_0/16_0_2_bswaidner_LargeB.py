def main(): 
	
	first_input = int(input())
	user_input = input()
		
	for n in range(first_input):

		input_list=[]
		
		ctr = 0
		input_string = user_input
		
		for i in range(len(input_string)):
			number = input_string[i:i+1]
			input_list.append((number))
		
		for j in range(1,len(input_list)):
			
			if input_list[j] != input_list[j-1]:
			
				if input_list[j] == "-":
					for z in range(0,j):
						input_list[z] = "-"
				elif input_list[j] == "+":
					for z in range(0,j):
						input_list[z] = "+"
				ctr+=1
				 
		if input_list[0] == "-":
			for a in range(len(input_list)):
				input_list[a] = "+"
			ctr+=1

		print("Case #", n+1, ": ", ctr, sep = '')

		if n == (first_input - 1):
			continue
		else:	
			user_input = input()
	
main()