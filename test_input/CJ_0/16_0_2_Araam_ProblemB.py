if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		with open('output.txt', 'w') as o:
			lines_list = f.read().splitlines()[1:]
			for idx, pancakes in enumerate(lines_list):
				num_flips = 0
				index = 0
				curr_pancake = pancakes[0]
				for pancake in pancakes:
					if pancake != curr_pancake:
						curr_pancake = pancake
						num_flips += 1
				if curr_pancake == '-':
					num_flips += 1
				o.write('Case #{}: {}\n'.format(idx + 1, num_flips))