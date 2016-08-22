from __future__ import print_function
from collections import deque


def abc_task(input_file, output_file):
    with open(input_file) as input_f:
        with open(output_file, 'w') as output_f: 
            n = input_f.readline().strip()
            mas = input_f.read().split('\n')
            result_mas = []
            for i, elem in enumerate(mas):
            	result = deque()
            	for letter in elem:
            		if result == deque([]):
            			max_letter = letter
            			result.extend(letter)
            		elif ord(letter) >= ord(max_letter):
            			max_letter = letter
            			result.appendleft(letter)
            		elif ord(letter) < ord(max_letter):
            			result.extend(letter)
            	result_mas.append(''.join([elem for elem in result]))
            for i, elem in enumerate(result_mas):
            	print("Case #{}: ".format(i+1) + str(elem),
                      file=output_f)