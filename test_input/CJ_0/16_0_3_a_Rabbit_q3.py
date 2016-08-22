from time import time
TIME_OUT = 0.01 # give up if execeeding timeout

def find_divisor(num,start_time):
    if num <= 3:
        return None
    elif num % 2 == 0:
        return 2
    elif num % 3 == 0:
        return 3
    i = 5
    while i * i <= num:
        if time() - start_time > TIME_OUT:
            return None
        if num % i == 0:
            return i
        elif num % (i + 2) == 0:
            return i + 2
        i += 6
    return None

def divisor_in_all_base(bin_num_str,start_time):
    result = []
    for i in xrange(2,11):
        res = find_divisor(int(bin_num_str, i),start_time)
        if res: # not a prime number, store the divisor
            result.append(res)
        else: # is a prime number, abort
            return None
    return result

def main():
    num_input = int(raw_input())
    for test_case_num in xrange(1, num_input + 1):
        
        length, num_coins = [int(i) for i in raw_input().strip().split(' ')]
        
        begin = ['0'] * length
        begin[0] = '1' # must start with 1
        begin[-1] = '1' # must end with 1

        begin_bin = ''.join(begin)
        end_bin = ''.join(['1']*length)

        begin = int(begin_bin,2)
        end = int(end_bin,2)

        count = 0

        print 'Case #%d:' % test_case_num
        for i in xrange(begin, end + 1, 2): # step 2 so it will always end with 1 in binary
            bin_num_str = '{0:b}'.format(i)
            result = divisor_in_all_base(bin_num_str,time())

            if result:
                count += 1                
                print '%s %s' % (bin_num_str, ' '.join([str(i) for i in result]))
            if count == num_coins:
                break


if __name__ == '__main__':
    main()