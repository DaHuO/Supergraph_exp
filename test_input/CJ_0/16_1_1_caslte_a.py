
def write_answer(index, answer):
    print("Case #%s: %s" % (index, answer))



def main():
    f = open("a.in")

    lines = f.readlines()
    case = lines[0].rstrip()


    for index in range(1, int(case) + 1):
        line = lines[index].rstrip()
        result = []

        for w in line:
            if len(result) > 0:
                result2 = []
                for wo in result:
                    result2.append(wo+w)
                    result2.append(w+wo)
                result = result2
            else:
                result.append(w)

        result.sort()

        write_answer(index, result[len(result)-1])


    f.close()


main()


