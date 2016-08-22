#read input file 
with open('input.txt') as input_file:
    lines = input_file.readlines()
    
txt = open("output.txt", "ab")

case = []
N_lines = 1
N_case = int(lines[0])


for i in range(1,N_case+1):
    case.append(lines[i])

for i in range(0, N_case):
    chars =[]
    for ch in case[i]:
        if ch == '\n':
            break
        if len(chars) < 1 :
            chars = ch
        else:
            if ord(ch) >= ord(chars[0]):
                chars = ch + chars
            else:
                chars = chars + ch
    output =  "Case #"+str(i+1)+": "+chars+"\n"
    print output
    txt.write(output)
txt.close()
                

    
        
