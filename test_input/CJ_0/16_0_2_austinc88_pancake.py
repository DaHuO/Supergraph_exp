if __name__ == "__main__":

    import fileinput
    import re
    input_file = fileinput.input()

    def flip(val):
        if val == 0:
            return 1
        return 0

    T = int(input_file.readline())
    output_f = open('B-large.out','w+')

    for case in range(1,T+1):
        val = str(input_file.readline())
        bin_val = re.sub('-', '0', re.sub('\+', '1', val))
        int_array = map(int, list(bin_val.rstrip()))
        
        all_ones = re.sub('0', '1', bin_val)
        int_ones_array = map(int, list(all_ones.rstrip()))
        counter = 0
        index = 0
        int_array = int_array[::-1]

        while int_array != int_ones_array:
            if int_array[index] == 0:
                for ind in range(index, len(int_array)):
                    int_array[ind] = flip(int_array[ind])
                    print int_array
                counter += 1
            else:
                index += 1


        output_f.write("Case #{0}: {1}\n".format(case, counter))

    output_f.close()