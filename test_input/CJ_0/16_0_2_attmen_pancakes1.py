f = open('C:\\study\\gjam\\jam2016\\B-large.in')
f_out = open('C:\\study\\gjam\\jam2016\\res.txt','w+')

T = int(f.readline())


def calc_min(inp):
    inp_len = len(inp)
    
    start_pos = 0
    cur_pos   = 1
    sign_change_cnt = 0
    while (cur_pos < inp_len):
        if (inp[cur_pos] != inp[start_pos]):
            start_pos = cur_pos
            sign_change_cnt += 1
        cur_pos += 1
    
    if (inp[-1] == '-'):
        sign_change_cnt += 1
    
    return sign_change_cnt        
    
    

for i in range(T):
    inp = f.readline()
    if (i < T-1):
        inp = inp[:-1]
    res = calc_min(inp)
    f_out.write("Case #"+str(i+1)+": "+str(res)+'\n')

f.close()
f_out.close()