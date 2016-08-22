def is_prime(num):
    if(num == 1 or num == 2):
        return(-1)
    
    num = decimal.Decimal(num)
    upper_bound = long(math.ceil(math.sqrt(num)))
    i = long(2)
    
    while(i <= upper_bound):
        if(long(num) % i == 0):
            return(i)
        if(i > 10000):
            return(-1)
        i += 1
        
    return(-1)

def calc_base(coin_str, base):
    coin = list(coin_str)
    base = long(base)
    
    total = long(0)
    for i,j in enumerate(coin):
        total += long(int(j) * (base ** (len(coin) - 1 - i)))
        
    return(total)

def is_jam_coin(coin_str):
    if(coin_str[0] != '1' or coin_str[-1] != '1'):
        return([])
    
    divisor_list = []
    
    for base in np.arange(2, 11):
        base_total = calc_base(coin_str, base)
        divisor = is_prime(base_total)
        if(divisor == -1):
            return([])
        else:
            divisor_list.append(divisor)
            
    return(divisor_list)

def gen_jam_coin(coin_len):
    num = []
    
    for i in np.round(np.random.rand(coin_len - 2)):
        num.append(str(int(i)))
    num = ''.join(num)
    return('1'+num+'1')

g = open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\coin\coin_small_out.txt','w+')

with open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\coin\C-small-attempt0.in', 'r+') as f:
    num_cases = int(f.readline())
    
    for i in range(num_cases):
        jam_len, num_jam = f.readline().split(' ')
        jam_len, num_jam = int(jam_len), int(num_jam)
        
        g.write('Case #' + str(i+1) + ':\n')
        count = 0
        
        jam_coin_list = []
        while(len(jam_coin_list) < num_jam):
            count += 1
            if(count > 10000):
                break
            jam_coin = gen_jam_coin(jam_len)
            
            if(jam_coin not in jam_coin_list):
                divisors = is_jam_coin(jam_coin)
                
                if(len(divisors) == 9):
                    divisors_str = [str(i) for i in divisors]
                    divisors_str = ' '.join(divisors_str)
                    
                    jam_coin_list.append(jam_coin)
                    g.write(jam_coin + ' ' + divisors_str + '\n')
        
g.close()