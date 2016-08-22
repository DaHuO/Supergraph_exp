if __name__ == "__main__":

    import fileinput

    from math import floor
    from math import sqrt
    import math

    def smallestDivisor(n):
        if n % 2 == 0:
            return 2
        else:
            squareRootOfn = int(floor(sqrt(n)))
            for i in range(3,squareRootOfn+1,2):
                if n % i == 0:
                    return int(i)
                    break
                else:
                    if i == squareRootOfn:
                        return 1

    def numberToBase(n, b):
        power = 0
        sum_return = 0
        while n:
            sum_return += int(math.pow(b, power)) * int(str(n)[-1])
            n /= 10
            power += 1
        return sum_return

    def checkNum(n):
        values = []
        for base in range(2,11):
            small = smallestDivisor(numberToBase(n, base))
            if small == 1 or small is None:
                return False
            values.append(small)
        return values

    def per(n):
        array_values = []
        for i in range(1<<n):
            s=bin(i)[2:]
            s='0'*(n-len(s))+s
            work_list = map(int,list(s))
            work_list.insert(0,1)
            work_list.append(1)
            work_value = int("".join(map(str, work_list)))
            array_values.append(work_value)
        return array_values

    input_file = fileinput.input()

    T = int(input_file.readline())
    output_f = open('C-small-attempt0.out','w+')
    output_f.write("Case #{0}:\n".format(1))
    for case in range(1,T+1):
        test_case = input_file.readline().split(" ")
        N = int(test_case[0])
        J = int(test_case[1])
        middle_length = N - 2

        array_test = per(middle_length)
        counter = 0
        for val in array_test:
            if counter > J-1: 
                break
            result = checkNum(val)
            if result is not False:
                output_f.write( str(val) + " " + " ".join(map(str,result)) + "\n")
                counter += 1

        

    output_f.close()