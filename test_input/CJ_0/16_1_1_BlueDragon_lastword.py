def main():
    file = open("/home/aidan/Documents/codejam161A/A-large.in")
    outFile = open("/home/aidan/Documents/codejam161A/A-large.out", "w")
    file.readline()
    for i, line in enumerate(file):
        string = ""
        string += line[0]
        for c in line[1:]:
            if c >= string[0]:
                string = c + string
            else:
                string += c
        outFile.write("Case #{}: {}".format(i+1, string))


if __name__ == "__main__":
    main()

