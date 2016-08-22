from itertools import groupby

def remove_last_pluses(my_list):
    if my_list[-1] == '+':
        my_list.pop()
        if my_list :
            return remove_last_pluses(my_list)
        else :
            return []
    else :
        return my_list
        
t = int(input())
input_list = []
for j in range(1, t + 1):
    ip = str(input())
    input_list.append(ip) 
    
for ul in input_list:
    k = remove_last_pluses(list(ul))
    short_list = [x[0] for x in groupby(k)]
    n = len(short_list)
    print("Case #{}: {}".format(input_list.index(ul)+1, n))