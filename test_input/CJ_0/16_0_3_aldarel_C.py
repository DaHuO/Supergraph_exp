import numpy

def convert_to_dec(string, base):
    digits = list(string[::-1])
    res = 0
    for i in range(len(digits)):
        res = res + int(digits[i])*numpy.power(base, i)
    return res

def combinations_get(str, m, i):
    combinations = list()
    if i == m:
        combinations.append(str)
    if i < m:
        one_str = str + "11"
        zero_str = str + "00"
        combinations.extend(combinations_get(one_str, m, i+1))
        combinations.extend(combinations_get(zero_str, m, i+1))
    return combinations

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        n, j = [int(s) for s in raw_input().split(" ")]
        
        """"for k in range(2, 11):
            res = convert_to_dec("100001", k)
            print(res, res%(k+1)==0 )"""
        if n%2 == 0:
            combinations = combinations_get("", n/2 - 2, 0)
            counter = 0
            comb_group_1 = list()
            comb_group_2 = list()

            for item in combinations:
                comb_group_1.append("11%s11" % str(item))
                comb_group_2.append("10%s01" % str(item))

            print('Case #%s:' % str(i))
            for item in comb_group_1:
                print("%s %s" % (item, "3 4 5 6 7 8 9 10 11"))
                counter = counter + 1
                if counter == j:
                    break
            if counter != j:
                for item in comb_group_2:
                    print("%s %s" % (item, "3 4 5 6 7 8 9 10 11"))
                    counter = counter + 1
                    if counter == j:
                        break
                if counter != j:
                    print("NEED MORE")