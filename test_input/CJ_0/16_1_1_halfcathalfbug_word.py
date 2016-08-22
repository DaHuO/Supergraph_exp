import sys

case = 0
for line in sys.stdin:
    if case == 0:
        case += 1
        continue

    output = "Case #%d: " % case

    curr = ""
    for c in line:
        curr = max(c + curr, curr + c)

    output += curr.strip()

    print output

    case += 1
