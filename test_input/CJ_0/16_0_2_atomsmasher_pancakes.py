import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--input-file', dest='fin', action="store", help="Input file")
parser.add_argument('--output-file', dest='fout', action="store", help="Output file")

args = parser.parse_args()

T = None
line_counter = 0
data = []
outputs = []

with open(args.fin) as infile:
    for line in infile:
        line_counter += 1

        if line_counter == 1:
            T = int(line)
            continue

        data.append(line.rstrip())

case_counter = 0

for item in data:
    case_counter += 1
    flips = 0
    stack = []

    if "-" not in item:
        outputs.append("Case #" + str(case_counter) + ": " + str(flips))
        continue

    if len(item) == 1:
        if item == "-":
            flips += 1

        outputs.append("Case #" + str(case_counter) + ": " + str(flips))
        continue

    for ch in item:
        stack.append(ch)

    current_sign = stack[0]
    i = 1
    while i < len(stack):
        if current_sign != stack[i]:
            flips += 1
            current_sign = stack[i]
        i += 1

    if current_sign == "-":
        flips += 1

    outputs.append("Case #" + str(case_counter) + ": " + str(flips))

with open(args.fout, "w") as output:
    for out in outputs:
        output.write("%s\n" % out)
        print out
        


                
    
