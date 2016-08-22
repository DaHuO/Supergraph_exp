
def reverse_stack(string,index):
	if index==0:
		return string
	return string[0:index][::-1].replace("-","*").replace("+","-").replace("*","+")+string[index:len(string)]


def find_solution(string):
	new_string=""
	for char in string:
		if new_string=="" or new_string[0]<=char:
			new_string=char+new_string
		else:
			new_string=new_string+char		

	return new_string




input_file = open('A-large.in', 'r')
output_file = open('A-large.out', 'w')

test_cases=int(input_file.readline())
for t in range(0,test_cases):
	string=input_file.readline()
	
	res=find_solution(string)		
	output_file.write("Case #{case}: {res}".format(case=t+1,res=res))

	if t<test_cases-1:
		output_file.write("\n")


	


