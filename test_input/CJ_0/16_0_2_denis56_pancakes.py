def main(input_file):
    with open(input_file,"r") as f:
        l = f.readlines()
        n = int(l[0])
        problems = []
        for i in range(n):
            problems.append([True if s == "+" else False for s in l[i+1].strip()])

    output = ""
    t = 1
    for p in problems:
        pn = len(p)

        v = 0 if p[0] else 1
        first = 0
        for i in range(pn):
            if p[i]:
                first = i
                break
            first = pn
        if first < pn:
            for i in range(first,pn):
                if p[i-1] and not p[i]: v+=2

        output += "Case #%d: %d \n" % (t,v)
        t += 1
    return output

if __name__ == "__main__":
    file_input = "b-large"
    output = main(file_input)
    print output
    with open(file_input + "_out", "w") as f:
        f.write(output)