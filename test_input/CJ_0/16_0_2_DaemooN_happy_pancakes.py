if __name__=="__main__":
    input_name = "input/2-small.in"
    output_name = "out.tmp"
    file = open(input_name, "r")
    file_out = open(output_name, "w")
    test_cases = int(file.readline())
    for test in range(1, test_cases + 1):
        inp = list(file.readline())[:-1]
        counter = 0
        prev = inp[0]
        for pancake in inp:
            if prev != pancake:
                counter += 1
            prev = pancake
        if prev == "-":
            counter += 1
        print("Case #" + str(test) + ": " + str(counter))

