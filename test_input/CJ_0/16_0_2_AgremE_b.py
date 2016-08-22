input_file = open("B-large.in")
output_file = open("solution.txt", "w")
t = int(input_file.readline().strip())
for i in range(t):
    output_file.write("Case #" + str(i+1) + ": ")
    s = input_file.readline().strip()
    total_flip = 0
    sign = s[0]
    for index in range(1,len(s)):
        if sign != s[index]:
            total_flip += 1
            sign = s[index]
    if s[-1] =='-':
        total_flip+=1
    output_file.write(str(total_flip))
    output_file.write("\n")
output_file.close()