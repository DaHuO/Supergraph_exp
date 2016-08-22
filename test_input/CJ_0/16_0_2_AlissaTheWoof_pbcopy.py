out =open('./pbout.txt', 'w+')
t = int(input())

def opposite(input):
	if input == "+":
		return "-"
	else: 
		return "+"

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def flip(pancake_placement, level):
	temp = []
	for a in range(0,level):
		temp.append(opposite(pancake_placement[a]))
	temp.reverse()
	for b in range(level, len(pancake_placement)):
		temp.append(pancake_placement[b])
	return temp


for x in range(0, t):
	out.write("Case #" + str(x+1) + ": ")
	total_list = [list(raw_input())]
	perfect = ["+" for i in range(len(total_list[0]))]
	flips = 0
	while perfect not in total_list:
		flips+=1
		copy = total_list
		total_list = []
		for some_position in copy:
			for place in range(1,len(some_position)+1):
				total_list.append(flip(some_position, place))
		total_list = uniq(total_list)
	out.write(str(flips)+ "\n")
