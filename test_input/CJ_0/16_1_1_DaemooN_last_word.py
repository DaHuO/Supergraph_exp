if __name__=="__main__":
    input_name = "A-small.in"
    output_name = "out.tmp"
    file = open(input_name, "r")
    file_out = open(output_name, "w")
    test_cases = int(file.readline())

    for test in range(1, test_cases+1):
        inp = list(file.readline()[:-1])
        first_letter = ""
        result = []
        for i in inp:
            if first_letter == "":
                first_letter = i
                result = [i]
            elif i >= first_letter:
                result = [i] + result
                first_letter = i
            else:
                result = result + [i]
        res = "".join(result)
        print("Case #" + str(test) + ": " + res)






