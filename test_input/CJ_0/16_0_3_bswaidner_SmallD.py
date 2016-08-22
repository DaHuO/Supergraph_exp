import random

def jamcoin(lst,num):
		
	for j in range(len(lst)):
		lst[j] = str(int(lst[j]) * ((num ** ((len(lst) - 1) - j))))
	_sum = 0
	for i in range(len(lst)):
		_sum += int(lst[i])

	return _sum
		
def generate_divisor(num):
	
	is_prime = True

	for q in range(2, 500):
		if num % q == 0:
			example = q
			is_prime = False
		
	if is_prime:
		return 0
	else:
		return example		
	
def main():
	
	jamcoin_list = []
	
	T = int(input())
	N_J = input()
	listN_J = N_J.split()
	
	N = int(listN_J[0])
	J = int(listN_J[1])
	
	for t in range(T):
		print("Case #", t+1, ":", sep = '')
		
		for j in range(J):
			answer = 0
			is_jamcoin = False
			
			while not(is_jamcoin):
				jc_list = ["1"]
				for i in range(N-2):
					jc_list.append(random.choice(["0", "1"]))
				jc_list.append("1")

				possible_jamcoin = "".join(jc_list)

				jc_list2 = list(jc_list)
				jc_list3 = list(jc_list)
				jc_list4 = list(jc_list)
				jc_list5 = list(jc_list)
				jc_list6 = list(jc_list)
				jc_list7 = list(jc_list)
				jc_list8 = list(jc_list)
				jc_list9 = list(jc_list)
				jc_list10 = list(jc_list)

				check_2 = jamcoin(jc_list2, 2)
				check_3 = jamcoin(jc_list3, 3)
				check_4 = jamcoin(jc_list4, 4)
				check_5 = jamcoin(jc_list5, 5)
				check_6 = jamcoin(jc_list6, 6)
				check_7 = jamcoin(jc_list7, 7)
				check_8 = jamcoin(jc_list8, 8)
				check_9 = jamcoin(jc_list9, 9)
				check_10 = jamcoin(jc_list10, 10)

				ex2 = generate_divisor(check_2)
				ex3 = generate_divisor(check_3)
				ex4 = generate_divisor(check_4)
				ex5 = generate_divisor(check_5)
				ex6 = generate_divisor(check_6)
				ex7 = generate_divisor(check_7)
				ex8 = generate_divisor(check_8)
				ex9 = generate_divisor(check_9)
				ex10 = generate_divisor(check_10)

				if (ex2 != 0) and (ex3 != 0) and (ex4 != 0) and (ex6 != 0) and (ex7 != 0) and (ex8 != 0) and (ex9 != 0) and (ex10 != 0):
					
					is_jamcoin = True
					for i in range(len(jamcoin_list)):
						if possible_jamcoin == jamcoin_list[i]:
							is_jamcoin = False
					if is_jamcoin != False:
						answer = possible_jamcoin
						jamcoin_list.append(answer)
						print(answer, ex2, ex3, ex4, ex5, ex6, ex7, ex8 , ex9 , ex10)
				else: 
					is_jamcoin = False
					
					
main()

	
	
	
	
